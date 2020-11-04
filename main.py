from Link import *
from Demand import *
from Variable import *
from itertools import groupby

def initProgram():
    linksTxt = "txtFiles/links.txt"
    demandsTxt = "txtFiles/demands.txt"
    links = []
    demands = []
    variables = []
    with open(linksTxt, "r") as f:
        line = f.readline()
        while(line):
            txtParsed = line.strip().split(" ")
            link = Link(txtParsed[0], txtParsed[1], txtParsed[2])
            links.append(link)
            line = f.readline()

    with open(demandsTxt, "r") as f:
        line = f.readline()
        while(line):
            txtParsed = line.strip().split(" ")
            demand = Demand(txtParsed[0], txtParsed[1], txtParsed[2])
            demands.append(demand)
            line = f.readline()

    for link in links:
        for demand in demands:
            firstElementOfDemand = demand.firstElement
            lastElementOfDemand = demand.lastElement
            if (link.lastElement != demand.firstElement and link.firstElement != demand.lastElement):
                variable = Variable(link, demand)
                variables.append(variable)

    outputFile = "output.lp"
    temp = []
    with open(outputFile, "w+") as f:
        for demand in demands:
            print("DEMAND: " + str(demand))
            variablesByDemand = getVariablesByDemand(variables, demand)
            string = ""
            for variableDemand in variablesByDemand:
                if variableDemand.link.firstElement == demand.firstElement:
                    print(variableDemand)
                   # string += str(variableDemand) + " + " variableDemand.demand.getVolume()
            for variableDemand in variablesByDemand:
                if variableDemand.link.lastElement == demand.lastElement:
                    print(variableDemand)

            intermediateVariables = getIntermediateVariables(variables, demand)
            print("INTERMEDIATES")
            for element in intermediateVariables:
                print("POSITIVE")
                for y in element[0]:
                    print(y)
                print("NEGATIVE")
                for k in element[1]:
                    print(k)


def getNegativeIntermediateVariables(variables, lastElement, demand):
    result = []
    for variable in variables:
        if (variable.demand == demand):
            if (variable.link.lastElement == lastElement):
                result.append(variable)
    return result


def getIntermediateVariables(variables, demand):
    tempResult = []
    for variable in variables:
        if(variable.demand == demand):
            #positive variables
            if(variable.link.firstElement != demand.firstElement and variable.link.firstElement != demand.lastElement):
                    tempResult.append(variable)

    #group variables that have the same first element
    groupsFirstElement = groupby(tempResult, lambda a: (a.link.firstElement))

    #row with two elements;
    #[0] = positive variables
    #[1] = negative variables
    #result will contain n rows, for each intermediate variable
    #in the 1-2-3-4 example, result will contain 3 and 4 for the 12 demand, and 2 and 3 for the 14 demand
    j = 1
    result = []
    for key, group in groupsFirstElement:
        positive = []
        row = []
        for element in group:
            positive.append(element)
        #we just need one of the element inside the group, so take the last one
        #no need for this to be inside the for loop
        negative = getNegativeIntermediateVariables(variables, element.link.firstElement, demand)
        row.append(positive)
        row.append(negative)
        j = j + 1
        result.append(row)

    return result


def getLinksByFirstElementOfDemand(links,demand):
    result = []
    for link in links:
        if(link.firstElement == demand):
            result.append(link)
    return result

def getVariablesByDemand(variables, demand):
    result = []
    for variable in variables:
        if(variable.demand == demand):
            result.append(variable)
    return result

if __name__ == '__main__':
    initProgram()
