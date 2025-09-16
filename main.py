from pyscript import display, document

def adding_numbers(e):
    a = float(document.getElementById('a').value)
    b = float(document.getElementById('b').value)
    h = float(document.getElementById('h').value)

    Area = ((a + b) / 2) * h   # trapezoid area formula

    display(f'The area of the trapezoid is {Area}', target='output')