
#checmking status of service###
def main():
    service_name =  's'
    service_status = statusof(service_name)
    print("status {} is {}".format(service_name,service_status))




def statusof(service_name):
    services ={
        "RDS": "running",
        "s3": "maintanance",
        "vpc": "running",

    }
    for key,value in services.items():
        if key == service_name:
            return services[service_name]
        
    #return "we dont have that service"


if __name__ == '__main__':
    main()



