words = ['Bootstrap (Twitter)', 'Apache Commons Codec', 'Commons IO', 'Apache Commons Lang', 'Apache Commons Logging', 'Apache HttpComponents Client', 'SLF4J API Module', 'Guava: Google Core Libraries for Java', 'Spring Framework', 'jackson-databind', 'JUnit', 'Visionmedia Debug', 'jackson-annotations', 'Apache Commons Collections', 'jQuery UI', 'ASM', 'BabelJs', 'node-uuid', 'FindBugs jsr305', 'Javassist', 'Commander.js', 'JavaBeans Activation Framework', 'Apache Commons Compress', 'UglifyJS', 'AOP Alliance', 'LessCss', 'yargs', 'Apache Xalan (Java)', 'range-parser', 'Apache Ant']

daSearch = open("NVD_Dashboard-Mapping.html", "r").read()

for word in words:
    if word in daSearch:
       print(word)
#    else:
#       print("not found")

print("\nDone")