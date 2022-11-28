# hf_project

## Description:

This simple web app uses FastAPI to display the contents of the HuggingFace dataset Rotten Tomatoes found here (https://huggingface.co/datasets/rotten_tomatoes) and searches the contents.
I downloaded the dataset locally first and added the contents into the container but this can be improved by creating an AWS database so the contents do not run on startup.

The app utilizes Docker to containerize the methods/endpoints and creates an app backend database using SQLAlchemy. The two methods are:

###  Methods 

#### /records/:

Get method with no inputs

Returns 5 random records

#### /query_substring/{substring}:

Input: Text string for searching on text field

Returns up to 5 random records containing that string

### Local Deployment

First ensure Docker is locally deployed and build the image by running the command 
```docker build -t hf_project:1.0 .```

Then, build the container 
```docker run --name hf_project -d -p 80:8000 hf_project:1.0```

The app should route to test on http://localhost/docs

### AWS Deployment

I aim to deploy on an AWS EC2 instance shortly

