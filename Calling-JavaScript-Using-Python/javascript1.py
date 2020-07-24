import js2py

js = """
function escramble_758(){
var side1 = 5; 
var side2 = 6; 
var side3 = 7; 
var s = (side1 + side2 + side3)/2;
var area =  Math.sqrt(s*((s-side1)*(s-side2)*(s-side3)));
document.write(area)
}
escramble_758()
""".replace("document.write", "return ")

result = js2py.eval_js(js)
print(result)