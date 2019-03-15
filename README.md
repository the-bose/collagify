# Collagify
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://www.youtube.com/watch?v=JkoM7CuOUFk)
[![forthebadge](https://forthebadge.com/images/badges/built-by-hipsters.svg)](https://www.youtube.com/watch?v=u1qN6gLbUMw)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Description
Collagify is a collage creator built with Python and Pixabay API. Collagify randomly generates **artsy** (I believe it's artsy) collages based on given keyword with the help of Pixabay API and employs a monocolour background.

### Pixabay API
[![Pixabay](https://pixabay.com/static/img/logo.png)](https://pixabay.com/)
* Pixabay is a vibrant community of creatives, sharing copyright free images and videos. All contents are released under the Pixabay License, which makes them safe to use without asking for permission or giving credit to the artist - even for commercial purposes.
* All images employed by Collagify are under [Pixabay License](https://pixabay.com/service/license/)
* **YOU NEED A PIXABAY API KEY FOR COLLAGIFY TO WORK**. Get your key [here](https://pixabay.com/api/docs/)

## Installation
* Clone repository
```sh
  git clone https://github.com/the-bose/collagify.git
```
* Create virtual environment
```sh
virtualenv venv
```
* Activate virtual environment
  * **Linux**
  ```sh
    source venv/bin/activate
  ```
  * **Windows**
  ```sh
    venv\Scripts\activate.bat
  ```
* Install dependencies
```sh
  pip install -r requirements.txt
```

## Running Collagify
* **YOU NEED A PIXABAY API KEY FOR COLLAGIFY TO WORK**. Get your key [here](https://pixabay.com/api/docs/). Edit the **app.py** file to include the key. Run the app.py file:
```sh
  python app.py
```
* Supply the keyword of collage when prompted. Wait for your random collages (yes, plural, as in 3) to be generated and voila!
* Output images are stored in the **/outputs/** folder with the keyword used to generate the collage in the file name.

[![forthebadge](https://forthebadge.com/images/badges/designed-in-ms-paint.svg)](https://www.youtube.com/watch?v=Gb2jGy76v0Y)
