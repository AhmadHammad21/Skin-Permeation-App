from jdk4py import JAVA, JAVA_HOME, JAVA_VERSION
from subprocess import check_output
import os


def extract_descriptors(smiles: str):
    T = " -cp extract_descriptors.jar extract_descriptors {}".format(smiles)
    return os.system(str(JAVA)+T)
