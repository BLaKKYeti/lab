class Agent:

    def __init__(self, runtime):
        self.runtime = runtime


    def run(self, task):

        if task == "find pdfs":

            result = self.runtime.execute(
                "filesystem",
                "list_pdfs"
            )

            return result


        return "I don't know how to perform that task yet"