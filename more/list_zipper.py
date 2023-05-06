"""
Illustrates the builtin zip() function by zipping two lists together into a list of tuples.
"""
import logging
import pathlib


def setup_logger(current_file):
    """
    Set up a custom logger for this file.
    @returns: the logger object and the name of the logfile.
    """
    logs_dir = pathlib.Path("logs")
    logs_dir.mkdir(exist_ok=True)
    module_name = pathlib.Path(current_file).stem
    logname = logs_dir.joinpath(module_name + ".log")
    logging.basicConfig(filename=logname, filemode="w", level=logging.DEBUG)
    logger = logging.getLogger(module_name)
    return logger, logname


def main(logger):
    xtimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    yvalues = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

    logger.info("xtimes = " + str(xtimes))

    zipped = zip(xtimes, yvalues)
    zipped_list = list(zipped)

    logger.info("zipped_list = " + str(zipped_list))

    with open("list_zipperout.csv", "w", newline="") as file_wrapper:
        file_wrapper.write("x,y\n")

        for row in zipped_list:
            x, y = row
            row_string = str(x) + "," + str(y) + "\n"
            file_wrapper.write(row_string)


if __name__ == "__main__":
    logger, logname = setup_logger(__file__)
    logger.info("Starting list_zipper.py")
    logger.info("Calling the main() function and passing in the logger")

    main(logger)

    logger.info(f"Script complete. See 'list_zipperout.csv' for output.")
    logger.info(f"Information is logged to: logs/{logname}")
    logger.info("The output file name is hardcoded and appears TWO TIMES in the script.")
    logger.info("This is a bad practice.")
    logger.info("Instead, we should set a variable just ONCE, and use the variable as needed.")
    logger.info("TODO: Edit the script to add a variable named outfile to hold the output file name.")
    logger.info("TODO: Edit the code in two places to use the variable instead of the hardcoded name.")
    logger.warn("Be careful. Indentation, spelling, and capitalization matter in Python.")

    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())
