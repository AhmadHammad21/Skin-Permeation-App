public class extract_descriptors {

    public static String printSmiles(String smiles) {
        String message = "Smiles is: " + smiles;
        return message;
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            String message = printSmiles(args[0]);
            System.out.println(message);
        } else {
            System.out.println("No Smiles provided.");
        }
    }
}
