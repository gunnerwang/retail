from subprocess import call, getoutput

host = "10.162.39.24:8000"
def upload_to_server(gender, age, time, product_name, product_price, file_name):
    data = {"gender": gender, "age": age, "during": time, "product_name": product_name, 
        "product_price": product_price, "file_name": file_name, "host": host}
    cmd = "curl -s -F gender={gender} -F age={age} -F during={during} -F product_name={product_name} -F product_price={product_price} -F face=@{file_name} http://{host}/demo/upload".format( **data )
    output = getoutput(cmd)
    print(output)