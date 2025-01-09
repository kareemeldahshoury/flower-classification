from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
  
  def __init__(self, in_features=4, h1=8, h2=9, out=3):
    super().__init__()
    self.fc1 = nn.Linear(in_features, h1)
    self.fc2 = nn.Linear(h1, h2)
    self.out = nn.Linear(h2, out)
    
  def forward(self, x):
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.relu(self.out(x))
    
    return x

torch.manual_seed(42)
model = Model()

model.load_state_dict(torch.load('../../../static/iris_neural_network.pt'))
model.eval()

app = Flask(__name__)
CORS(app) #Allows flask app to handle requests coming from different domains

@app.route("/predict", methods=["POST"])
def predict():
  data = request.json
  print(data)
  inputs = np.array(data['inputs'], dtype=np.float32) #change type of the inputs
  print(inputs)
  inputs = torch.tensor(inputs).unsqueeze(0) # turn the array into a tensor
  print(inputs)
  
  with torch.no_grad():
    outputs = model(inputs).numpy().tolist()
    print(f'outputs: {outputs}')
    outputs = torch.tensor(outputs).unsqueeze(0)
    print(f'tensor outputs: {outputs}')
    
  predicted_class = torch.argmax(outputs).item()
  print(f'predicted output: {predicted_class}')
  
  if predicted_class == 0:
    return jsonify({'prediction': "Setosa"})
  elif predicted_class == 1:
    return jsonify({'prediction': "Versicolor"})
  else:
    return jsonify({'prediction' : "Virginica"})
    
if __name__ == "__main__":
  app.run(debug=True)
      
    
    