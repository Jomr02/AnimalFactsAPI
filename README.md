# 🐾 Animal Facts API

Welcome to the **Animal Facts API** repository! This simple project is designed to provide interesting and educational facts about animals via a simple RESTful API using Flask. Whether you're building a fun trivia app, learning about API development, or just love animals, this API has you covered!

---

## 🚀 Getting Started

Follow these steps to get the Animal Facts API up and running:

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Jomr02/AnimalFactsAPI.git
   cd AnimalFactsAPI
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the API server:
   ```bash
   python main.py
   ```

4. The server will start at `http://127.0.0.1:5000`.

---

## 📚 API Endpoints

### Get all Animal Fact
**GET** `http://127.0.0.1:5000/animalfacts/`
- **Description**: Returns a random animal fact.

**Example Response**:
```json
{
  "animal": "cat",
  "fact": "Cats sleep 70% of their lives."
}
```

### Get Fact by Animal
**GET** `http://127.0.0.1:5000/animalfacts/<animal>`
- **Description**: Returns a fact for the specified animal.

**Example**:
`GET http://127.0.0.1:5000/animalfacts/api/fact/dog`

**Response**:
```json
{
  "animal": "dog",
  "fact": "Dogs have three eyelids."
}
```

### Add fact by Animal
**POST** `http://127.0.0.1:5000/animalfacts/<animal>?fact=<fact>`
- **Description**: Save in the database a fact for the specified animal.

**Example**:
`POST http://127.0.0.1:5000/animalfacts/Dog?fact=Dogs Bark`

**Response**:
```
Fact succesfully created.DogDogsBark
```

---

