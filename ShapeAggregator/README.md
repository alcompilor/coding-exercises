**Note:** In C# / Java I would probably use Strategy Pattern + Method Overloading for this. Since Python doesn’t support method overloading, I ended up using a mapping approach which seems like one of the cleaner ways to do the task without ever modifying the original aggregator (doesn't violate SOLID's Open/Closed principle).

Run CLI:
```
python3 main.py --file ./shapes.json --output ./area.txt
```
![Demo Image](demo.png)

Run tests:
```
python3 -m unittest discover -s tests --verbose
```