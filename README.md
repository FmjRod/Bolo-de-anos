# Bolo-de-anos

# Installation

## Windows Install
### Install Python and set variables
* Install Python from the official website [here](https://www.python.org/downloads/), the version used on this project was 3.12.0, so that is the recommended version to use

* Next locate where the Python is installed, by opening cmd (You can do this by opening Windows search, Windows key + S, and then writing cmd and clicking), after it opens write "where python" and, if more than one result appear copy the one with the version on it (ex: `C:\Users\\[user]\AppData\Local\Programs\Python\Python312\python.exe`)

* Open Windows Search (Windows key + S) and search for "Edit the system enviroment variables"

* Select Enviroment variables

* On the system variables table (the bottom one) select the entry with the Variable "Path" and click "Edit"

* On the right side of the window click "New", then paste the Python path you copied earlier

### Install requirements
* Using cmd navigate to the directory of the project (ex: `cd Desktop\Bolo-de-anos`)

* Run the command `pip install -r requirements.txt`

## Linux Install
* The latest versions of GNU\Linux should come with a Python version installed, to check open the terminal and run: `which python3`

* If no version is installed or it is a different one than 3.12.0 (the recommended for this project) then run the following command: 
    - Debian and Ubuntu: `sudo apt-get install python3.12.0`
    - RedHat and CentOS: `sudo yum install python3.12.0`

### Install requirements
* Using the terminal navigate to the directory of the project (ex: `cd Desktop\Bolo-de-anos`)

* Run the command `pip install -r requirements.txt`


## MacOs Install
* Some versions of Mac OS came pre-installed with Python 2.7, to get Python 3.12.0 go to: https://www.python.org/downloads/mac-osx/

### Install requirements
* Using the terminal navigate to the directory of the project (ex: `cd Desktop\Bolo-de-anos`)

* Run the command `pip install -r requirements.txt`

# Explanation

* The program is split into 3 components:
    - Main: Which calls the threads of the other two components (Producer and Consumer)
    - Producer: Receives a list of urls and returns a Queue filled with lists composed of the url of a page and its markup code
    - Consumer: Receives the Queue resulting from the producer, checks if that Queue is empty and if an Event has been set (this event marks the end of the producer's work) if both of this conditions are true, the consumer finishes its work. The work consists on using [BeatifulSoups](https://www.crummy.com/software/BeautifulSoup/) library to extract the links from the markup and stores them in a list with the url from the page they belong to.

# Improvements
* The consumer could do threading itself to parse the urls independently instead of doing it one by one (This would need a the list to be shared between threads and synchronized, we could turn the list into a Queue/Dequeue and use a Lock to achieve this)

* Unit testing

* Save base urls and add them to the relative ones to get fully functioning urls in the list instead of relative ones
