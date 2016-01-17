def buildConnectionString(params):
    """Build a connectuion string from a dictionary of parameters.


    Return string. """

    return ";".join(["%s=%s" % (k, v) for k, v, in params.items()])

if __name__ == "__main__":
    myParams = {"server":"mpilgrim", \
                "database":"mater", \
                "uid":"sa", \
                "pwd": "secret" \
                }

    print (buildConnectionString(myParams))
