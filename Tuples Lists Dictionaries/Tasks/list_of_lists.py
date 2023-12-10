import copy

def enrollment_stats(list_of_universities):
    """Return two lists"""
    counts_of_students = [copy.deepcopy(list_of_universities[list_of_universities.index(element)][1]) for element in list_of_universities]
    price_of_study = [copy.deepcopy(list_of_universities[list_of_universities.index(element)][2]) for element in list_of_universities]
    return (counts_of_students,price_of_study)

def mean(list_of_mean):
    """Return mean meaning"""
    mean_meaning = sum(list_of_mean)/len(list_of_mean)
    return (mean_meaning)

def median(list_of_median):
    """Return median meaning"""
    list_of_median.sort()
    if len(list_of_median) % 2 == 0:
        medianan_meaning = (list_of_median[len(list_of_median)/2-1]+list_of_median[len(list_of_median)/2])/2
    else:
        medianan_meaning = list_of_median[len(list_of_median)//2]

    return (medianan_meaning)

universities = [
    ['California Institute of Technology',2174,37704],
    ['Harvard',19627,39849],
    ['Massachusetts Institute of technology',10566,40732],
    ['Princeton',7802,37000],
    ['Rice',5879,35551],
    ['Stanfod',19535,40569],
    ['Yale',11701,40500],
]


print(f"""
###########################################################
Total students: {sum(enrollment_stats(universities)[0]):,.0f}
Total tuition: ${sum(enrollment_stats(universities)[1]):,.0f}

Student mean: {mean(enrollment_stats(universities)[0]):,.2f}
Student median: {median(enrollment_stats(universities)[0]):,.0f}

Tuition mean: ${mean(enrollment_stats(universities)[1]):,.2f}
Tuition median: ${median(enrollment_stats(universities)[1]):,.0f}
###########################################################""")

