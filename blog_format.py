def format(dict):
    for i in dict:
        tag = (dict[i][0])

        dict[i][1] = ("<" + tag + ">" + dict[i][1] + "</" + tag + ">")

    return(dict)