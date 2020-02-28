# WikiCategories
# Setup
### This setup assumes you have docker, python and git installed on your machine

1. #### Clone this repository to your local machine
    ```sh
    git clone https://github.com/Klcsln/WikiCategories.git
    ```
2. #### Make sure you are in the correct working directory
    ```sh
    cd WikiCategories/
    ```
3. #### Run the run.sh bash script. This will setup everything automatically for you, you can check the commands run by opening run.sh on any text editor. A warning though, it will install the packages in requirements.txt globally without creating a virtual environment as I didn't want to spend more time figuring that out. It's 4 am. So I would recommend running everything in a virtual environment of your own. The following should do the trick
    ```sh
    pip install virtualenv
    virtualenv ../WikiCategories
    source bin/activate
    ``` 
    #### Make the shell script executable then run it
    ```sh
    chmod u+x run.sh
    ./run.sh wikipediaCategoryUrl
    ```
    e.g.
     ```sh
    ./run.sh https://en.wikipedia.org/wiki/Category:The_Lord_of_the_Rings
    ```
4. #### If you are running into permission issues with docker after running the bash script, make sure you can run docker without sudo using the following script
    ```sh
    sudo chmod 666 /var/run/docker.sock
    ```
5. #### At this point you can start exploring the data parsed from wikipedia by going into the docker interactive terminal and going into mongo shell
    ```sh
    docker exec -it categorydb bash
    mongo
    use categories_db
    db.parsed_categories.find()
    ```
6. #### When you are done exploring, you can stop and remove the docker image or restart it to access it later if you decide to not remove it.
    ```sh
    sudo docker stop categorydb
    sudo docker rm categorydb 
    OR 
    sudo docker start categorydb
    ```
