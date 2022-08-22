##from logging import *
###debug("This is Debug")
###info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

##import logging
##logging.basicConfig(filename="log1")
##warning("this is warning")
##error("this is error")
##critical("this is critical")



##
##from logging import *
##basicConfig(filename="logfile2303.log")
####debug("This is Debug")
####info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

##from logging import *
##basicConfig(filename="logfile2303.log", level=DEBUG)
##debug("This is Debug")
##info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

##from logging import *
##basicConfig(filename="logfile4303.log", level=DEBUG, filemode='w', format='%(asctime)s -- %(message)s')
##debug("This is Debug")
##info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

##from logging import *
##basicConfig(filename="logfile303.log", level=DEBUG, filemode='w')
##debug("This is Debug")
##info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

###6. FormatLogData2 (1).py

##from logging import *
##LOG_FORMAT = '%(asctime)s // %(message)s // %(lineno)d' 
##basicConfig(filename="logfile5.log", level=WARNING, filemode='w', format=LOG_FORMAT)
##debug("This is Debug")
##info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

##from logging import *
##LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}' 
##basicConfig(filename="logfile6.log", level=DEBUG, filemode='w', style='{', format=LOG_FORMAT)
##debug("This is Debug")
##info("This is Info")
##warning("This is Warning")
##error("This is Error")
##critical("This is Critical")

##from logging import *
##LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}' 
##basicConfig(filename="logfile7.log", level=DEBUG, filemode='w', style='{', format=LOG_FORMAT)
##logger = getLogger('Ojas')
##logger.debug("This is Debug")
##logger.info("This is Info")
##logger.warning("This is Warning")
##logger.error("This is Error")
##logger.critical("This is Critical")

##import logging
##logging.basicConfig(filename='employee.log',
##                     level=logging.INFO,
##                     format='%(lineno)s::%(asctime)s::%(levelname)s::%(message)s::%(name)s')
##logger = logging.getLogger('swetha')
##def validation(fun):
##    logger.info('Entered validation function')
##    def fun(user_input):
##        logger.info('Before Checking in Data')
##        data=['swetha']
##        if user_input in data:
##            logger.info('username present in database')
##            return 'welcome '+user_input
##        else:
##            logger.debug('username Not present in database')
##            return 'wrong user'
##    return fun
##@validation
##def login_user(user_input):
##    return user_input
##user_input=input("Enter UserName: ")
##logger.info('User Input given')
##print(login_user(user_input))
