# JSON

JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate.

## JSON in Python:

    import json

- to write:

        json.dump()

- to read:

        json.load()

    > OBS: json.load() automatically convert json file to python dictionaries

- to update:

        json.update()

## Writing dict to a json file:

    data = {
        "name": "Davi Belo",
        "age": 20
    }
    
    with open("02-intermediate/04b-example.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

## Other example:

> see 13-passwordManager project:

    try:
        with open(DATA_FILE, mode="r") as data_file:
            # reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        with open(DATA_FILE, mode="w") as data_file:
            # creating a data file and saving the new_data
            json.dump(new_data, data_file, indent=4)
    else:
        # updating data with new data
        data.update(new_data)
        with open(DATA_FILE, mode="w") as data_file:
            # saving updated data
            json.dump(data, data_file, indent=4)
    finally:
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)






