# MLOPS CI-CD Boston Housepricing Project

## About

A MLOPS CI-CD imlementaion of a **Linear Regression Machine Learning Model** that predicts house pricing in Boston Massachusetts based on various features.

The Kaggle [Dataset](https://www.kaggle.com/code/prasadperera/the-boston-housing-dataset) used contains information collected by the U.S Census Service concerning housing in the area of Boston.

The model is:

- Configured with a simple UI experience to predict house price based on user input
- Configured with an API endpoint to test & predict house prices
- Packaged by pickle
- Dockerized
- Implemented within a CICD pipeline using GitHub Actions
- Deployed on Heroku

---

## Used Tools and Technologies

| Tool/Technology                                         | About                                                                                            |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [Python](https://www.python.org/)                       | Programming language                                                                             |
| [Jupyter Notebook](https://jupyter.org/)                | Web-based interactive computing platform                                                         |
| [Pickle](https://docs.python.org/3/library/pickle.html) | Package used for serializing/converting a Python object into a byte stream to store it in a file |
| [Flask](https://flask.palletsprojects.com/)             | Micro web framework written in Python                                                            |
| [Docker](https://www.docker.com/)                       | Containerization Tool                                                                            |
| [Heroku](https://www.heroku.com/)                       | Hosting service                                                                                  |
| [GitHub Actions](https://github.com/features/actions)   | (CI/CD) platform                                                                                 |

---

## Note

**Heroku ended there free hosting plan recently but you can build the project locally and test it following the steps below.**

---

## Build Steps

- Clone the repository

  ```bash
  git clone https://github.com/ahmedfarag9/mlops-cicd-bostonhousepricing.git && \
  cd mlops-cicd-bostonhousepricing
  ```

- Build Docker image

  ```bash
  docker build -f Dockerfile -t bostonhousingprice .
  ```

- Start Docker container

  ```bash
  docker run --name bostonhousingprice -d -p 5000:5000 bostonhousingprice
  ```

- Then go to [http://localhost:5000/](http://localhost:5000/) in your browser of choice and Voila! your project is up and running.
- Test it with some values and see the results.

---

## Testing API endpoint with Postman

Send a POST request to this API endpoint: [http://localhost:5000/predict_api](http://localhost:5000/predict_api)

With the following JSON body:

```json
{
  "data": {
    "CRIM": "0.00632",
    "ZN": "18.0",
    "INDUS": "2.31",
    "CHAS": "0.0",
    "NOX": "0.538",
    "RM": "6.575",
    "AGE": "65.2",
    "DIS": "4.0900",
    "RAD": "1.0",
    "TAX": "296.0",
    "PTRATIO": "15.3",
    "B": "396.90",
    "LSTAT": "4.98"
  }
}
```

---

## Live Demo -- > [https://mlopscicdbostonhousepricing-ahmedfaraga12.b4a.run/](https://mlopscicdbostonhousepricing-ahmedfaraga12.b4a.run/)

<!-- 
### Implementaion inspired by [Krish C Naik](https://github.com/krishnaik06)
-->
