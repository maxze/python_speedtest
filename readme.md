# Speedtest Logger

This is a small and dirty script that runs a speedtest at set intervals. 
Configuration can be changed in the file ```configuration.py```. The script logs the results into a simple text file 
with each line being a json document representing one test result.

# Installation
- ```git clone https://github.com/maxze/python_speedtest.git```
- ``cd python_speedtest``
- ```pip install -r requirements.txt ```

# Usage

```python main.py```

There's also a ```statistics.py``` file which can be used to calculate the average of all results.
