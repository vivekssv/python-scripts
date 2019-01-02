### python-scripts

- first_helloworld.py
maintenance - Print hello world in console
- forloop1.py
maintenance - Array of index, forloop and if and else condition covered.
- functions.py
maintenance - Functions with input parms handle & handled format with multiple arugs in print
- create_directory.py
maintenance - creating the master directory and creating the child directory with array of objs
- variables_structure.py
maintenance - types of variable assignments
- dictionary.py
maintenance - collection of list how can proceed with it
- dictionary_json.py
maintenance - collection of json input to iterate into the python Dictionary 

### Docker images handle
- docker search newimages
- docker pull imagename
- docker run -it imagename /bin/bash
    run to activate 
    it - interactive session
    imagename - docker image
    /bin/bash (linux) or cmd (windows)
- docker ps
    will show current process
    (-a) will show all history
- docker exec 5dcfbe74e100container_id /usr/local/tomcat/bin/catalina.sh run
- docker run --rm -it -p 8443:8080 tomcat:latest
