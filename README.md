# binance-api

This is a repository that contains some instructions on setting up a Python 3 virtual enviorment -- to make package mangement easy for the Binance API. 

First, make sure you have Python 3 installed. Run:
```
python3 --version
```
You should see a version of python that starts with a 3. Then, make sure that pip 3 is installed. Run:
```
pip3 --version
```
It should exist and report back some version!

Now, we have can create a new Python virtual enviorment. A virutal enviorment is like a "box" for libraries to live in, and to run your code in. It will stop you from fucking up your computer when you're installing packages on it, and also it makes it easy for me to share the packges with you!

To make a Python 3 virtual enviorment, run (in this folder):
```
python3 -m venv .
```
You should see a `bin` and `lib` folder appear (and maybe some other things). We are now ready to "enter the safe box" - aka, run our virutal enviorment. To start the virtual enviorment, run
```
source bin/activate
```
This should add `(binance-api)` to the front of your Terminal prompt! 

Now that we are in our safe little box, we can start installing packages. Remember that these packages will only be installed in our little box, so the packages we install here can only be used while it's running (e.g. while the `(binance-api)` thing is in front of the terminal prompt).

To install the packages, use the command:
```
pip3 install -r requirements.txt
```
When you run this command, it should install a bunch of shit! And not fail...

Now, we need to add our Binance API Key and Secret to the project. To do this, create a file called `secrets.txt`, and add the key and secret, each in their own lines. The file should look like:
```
API_KEY
API_SECRET
```

Then, run:
```
python3 main.py
```
You should see your key and secret print out. And some data that is an actual API call on the Binance API!
