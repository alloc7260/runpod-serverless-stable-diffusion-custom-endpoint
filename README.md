1. download any base model for Ex. => sd_xl_base_1.0.safetensors
2. if you have any checkpoint model then take it along with base model for Ex. => sdxl-base-10000-000009.safetensors (Lora checkpoint)
3. the directory structure will look like this
```
        .
        ├── builder
        │   ├── cache.py
        │   ├── clone.sh
        │   └── requirements.txt
        ├── Dockerfile
        ├── imgs
        │   ├── create endpoint.png
        │   └── create template.png
        ├── README.md
        ├── requesting-script.py
        └── src
            ├── rp_handler.py
            └── start.sh
```
4. make changes in files like `Dockerfile` and `start.sh` according to your model names 
5. docker login
6. docker build -t alloc7260/sdxlbase1:v12 .     # put your username insted of alloc7260
7. docker push alloc7260/sdxlbase1:v12           # put your username insted of alloc7260
8. go to runpod console
9. go to serverless tab 
10. select custom template
11. create custom template using this public docker image
![Custom Template](https://github.com/alloc7260/runpod-serverless-stable-diffusion-custom-endpoint/blob/main/imgs/create%20template.png?raw=true "Create Template")
12. select endpoints
13. create endpoint by specifying created template name and instance details
![Custom Endpoint](https://github.com/alloc7260/runpod-serverless-stable-diffusion-custom-endpoint/blob/main/imgs/create%20endpoint.png?raw=true "Create Endpoint")
14. get the endpoint id and put it in `requesting-script.py`
15. get your api key from settings tab and put it in `requesting-script.py`
16. pip install requests opencv-python numpy Pillow 
17. tweak the parameters and run the script by `python3 requesting-script.py`
