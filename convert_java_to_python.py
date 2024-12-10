from jdk4py import JAVA, JAVA_HOME, JAVA_VERSION
import subprocess
import os


def extract_descriptors(smiles: str):
    # command = "java -jar DescriptorsGeneratorCLI-1.0.0.jar {}".format(smiles)
    command = ["java", "-jar", "DescriptorsGeneratorCLI-1.0.0.jar", smiles]

    print("command")
    print(command)
    # generated_descriptors = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    generated_descriptors = result.stdout

    descriptors_list = str(generated_descriptors).split(",")
    
    cleaned_smiles = str(descriptors_list[0]).replace("\r", "").replace("\\n", "").replace("b\'", "")
    clean_descriptors = descriptors_list[1:]

    clean_descriptors = [float(desc.replace("\'", "").replace("\\r", "").replace("\\n", "")) for desc in clean_descriptors]

    # adding temp 310 kelvin
    clean_descriptors.insert(0, 310)
    return cleaned_smiles, clean_descriptors
