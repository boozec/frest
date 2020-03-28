import os
from .bcolors import COLORS


ENDC = len(COLORS) - 1


def logging(text, _type=ENDC, end=""):
    print(f"{COLORS[_type]}{text}{COLORS[ENDC]}", end=end)


def logging_arg(text, *args):
    args = [f"{COLORS[0]}{i}{COLORS[ENDC]}" for i in args]
    print(text.format(*args), end="")


def logo():
    print(
        """  
   __               _    
  / _|             | |   
 | |_ _ __ ___  ___| |_ 
 |  _| '__/ _ \/ __| __| 
 | | | | |  __/\__ \ |_  
 |_| |_|  \___||___/\__|
    \n\n"""
    )


def inputsr():
    return input().strip().replace(" ", "_").lower()


def create_field(fields):
    field = {"name": "", "type": "", "nullable": True}
    logging("Choose field name: ")
    field_name = inputsr()
    while (len(field_name) < 1 or field_name[0].isdigit()) or (
        field_name in fields or field_name in ["id", "created_at", "updated_at"]
    ):
        if len(field_name) < 1 or field_name[0].isdigit():
            logging("Field name must not be empty or starts with a number", 2, "\n")
        else:
            logging("Field name already exists", 2, "\n")

        logging("Choose field name: ")
        field_name = inputsr()

    field["name"] = field_name

    logging("Choose field type: ")
    logging("int, str, text, datetime, float, bool", 0, " ")
    field_type = inputsr()
    if field_type not in ["int", "str", "text", "datetime", "float", "bool"]:
        logging("Field type must be one of the supported type", 2, "\n")
        logging("Choose field type: ")
        logging("int, str, text, datetime, float, bool", 0, " ")
        field_type = inputsr()

    if field_type == "str":
        logging("Choose string size: ")
        stringsize = inputsr()
        while not stringsize.isdigit():
            logging("String size must be an integer number", 2, "\n")
            logging("Choose string size: ")
            stringsize = inputsr()

        stringsize = int(stringsize)
        if stringsize < 1:
            logging("You inserted 0, so it will be 1 by default", 4, "\n")
            stringsize = 1

        field["size"] = stringsize

    field["type"] = field_type

    logging("Field is nullable? (Y/n): ")
    field_nullable = inputsr()

    if len(field_nullable) > 0:
        while True:
            if field_nullable[0] not in ["y", "n"]:
                logging("Field is nullable? (Y/n): ")
                field_nullable = inputsr()
            else:
                break

        if field_nullable[0] == "n":
            field["nullable"] = False

    return field


def create_model_cli(name):
    logging(
        "Fields id, created_at, updated_at are default on every new model, you can delete it from model file",
        4,
        "\n\n",
    )
    fields = []
    logging("Create field: (Y/n)")
    answer = inputsr()

    while answer in ["y", "", "yes"]:
        field = create_field(fields)
        fields.append(field)

        logging("Create new field: (Y/n)")
        answer = inputsr()

    return fields


def create_app(name):
    name = name.lower().replace('-', '_')

    if name.isdigit() or name[0].isdigit():
        logging("Name cannot be a number o starts with a number", 2)
        return

    if len(name) < 2:
        logging("Name of app must be minimun 2 characters long", 2)
        return

    if os.path.exists(f"scheme/{name}"):
        logging("App already exists", 2)
        return

    logging_arg("Create {}... ", f"scheme/{name}")
    os.mkdir(f"scheme/{name}")
    logging("OK", 3, "\n")

    logging_arg("Create {}... ", f"scheme/{name}/__init__.py")
    open(f"scheme/{name}/__init__.py", "w").close()
    logging("OK", 3, "\n")

    logging_arg("Create model for {}...\n", name)
    fields = create_model_cli(name)
    print(fields)
    logging("OK", 3, "\n")
