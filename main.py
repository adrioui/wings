from fastapi import FastAPI

from schema import TrainRequestBody, TrainResponse, PredictRequestBody, PredictResponse

import model

from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
def read_root():
    return {"Content": "Service is up and running."}


@app.post("/train", response_model=TrainResponse)
def create_train(request: TrainRequestBody) -> TrainResponse:
    # Access the request body
    request_data = request.data
    request_save_path = request.save_path

    # Encode the request model to raw json
    request_json = jsonable_encoder(request_data)

    # Train the data using given function
    accuracy = model.train(data=request_json, save_path=request_save_path)

    # Return the result
    response = TrainResponse(accuracy=accuracy, status="success")
    return response


@app.post("/predict", response_model=PredictResponse)
def create_predict(request: PredictRequestBody) -> PredictResponse:
    # Access the request body
    request_train = request

    # Encode the request model to raw json
    request_json = jsonable_encoder(request_train)

    # Predict the data using available model
    prediction_result = model.predict(request_json, "model1")

    # Return the prediction result
    response = PredictResponse(result=prediction_result, status="success")
    return response
