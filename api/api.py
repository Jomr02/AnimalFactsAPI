from flask import Flask, request, jsonify
from db import access_db

app = Flask (__name__)

@app.route('/animalfacts/', defaults={"animal_id": ""}) #This way, /animalfacts/ returns all rows
@app.route("/animalfacts/<animal_id>", methods=["GET"])
def get_facts (animal_id):

    facts = access_db.get_facts(animal_id)

    if facts:
        return jsonify(facts), 200
    else:
        return jsonify({"message": "No facts found for this animal: " + animal_id}), 404


@app.route("/animalfacts/<animal>", methods=["POST"])
def set_fact (animal):

    #Get fact parameter: E.G: /animalfacts/tiger?fact=Tiger Growl
    fact = request.args.get("fact")

    if not animal or not fact:
        return 'ERROR: Complete all data E.G /animalfacts/tiger?fact=Tiger Growl',400

    data_returned = access_db.insert_animal_fact(animal, fact)

    if 'ERROR' in data_returned:
        return data_returned, 200
    else:
        return data_returned, 201


if __name__ == "__main__":
    app.run(debug=True)




