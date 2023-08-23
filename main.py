try:
    print("1. initialize")
    try:
        import webview
        import sys
        print("   import modules [okay]")
    except Exception as e:
        print("   import modules [failed: " + str(e) + "]")
        print("2. exit")
        exit("   exit program")
    
    try:
        webview.create_window("Wildberries", "https://wildberries." + sys.argv[1])
        print("   make window [okay]")
    except Exception as e: 
        print("   make window [failed: " + str(e) + "]")
        print("2. exit")
        exit("   exit program [okay]")
    
    try:
        webview.start()
        print("   start window [okay]")
    except Exception as e:
        print("   start window [failed: " + str(e) + "]")
        print("2. exit")
        exit("   exit program")
    
    print("2. exit")
    print("   exit program [okay]")
except KeyboardInterrupt:
    print("2. exit")
    print("     exit program [okay]")