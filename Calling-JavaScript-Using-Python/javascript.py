import js2py

# This is a simple example of String Concatination
# using JavaScript.

js_code = """
function concat_2_strings_py(){
var a,b,c
a='+1 '
b='84-'
a+='425-'
b+='7450'
c='9'
document.write(a+c+b)
}
concat_2_strings_py()
""".replace("document.write", "return ")

result = js2py.eval_js(js_code)
print(result)