from flask import Flask
import json

app = Flask(__name__)

human_record = {}


@app.route("/fetch-data", methods=["POST"])
def fetch_data():
    with open("mock_data.json", "r+") as file:
        content = json.loads(file.read())
    index = len(human_record) + 1
    transformed_data = []
    for item in content:
        transformed_item = {}
        for key, value in item.items():
            transformed_item[key] = value.lower()
        transformed_data.append(transformed_item)

    human_record[index] = transformed_data

    return {
        "data": {"transformation_id": index},
        "error": False,
        "message": "Data fetched and transformed",
    }, 200


@app.route("/get-processed-data/<int:record_id>", methods=["GET"])
def get_transformed_data(record_id: int):
    data = human_record.get(record_id)
    if not data:
        return {
            "data": {},
            "error": True,
            "message": f"No data exists for the given record_id: {record_id}",
        }, 400
    return {
        "data": data,
        "error": False,
        "message": "",
    }, 200


if __name__ == '__main__':
    # Run the application on the local development server
    app.run(debug=True)
