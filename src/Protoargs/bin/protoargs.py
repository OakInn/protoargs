#!/usr/bin/python

import os
import sys
import logging

import protoargs_pa
import paLogger
import paCppGenerator
import paPyGenerator

class ArgsParser:

    def parse(self, argv):
        self.config = protoargs_pa.parse("protoargs", 
                "Protoargs program generates command line arguments parsers, using proto file as configuration.", argv)

if __name__ == "__main__":
    #import sys
    #reload(sys)
    #sys.setdefaultencoding('utf8')

    parser = ArgsParser()
    parser.parse(sys.argv[1:])

    # initialize logger
    paLogger.init(parser.config.loglevel, "/tmp");
    logging.info("Arguments parsed")

    # print configuration
    logging.debug(parser.config)

    if parser.config.cpp or parser.config.py:
        path = parser.config.src
        dst = parser.config.dst

        if parser.config.cpp:
            logging.info("Generate c++ parser from proto file '" + path + "'")
            generator = paCppGenerator.Generator(path, dst)
            generator.generate()

        if parser.config.py:
            logging.info("Generate python parser from proto file '" + path + "'")
            generator = paPyGenerator.Generator(path, dst)
            generator.generate()

    else:
        logging.critical("Specify at least one parser language to proceed (e.g '--cpp'). Use '-h|--help' for help.")
        sys.exit(1)
