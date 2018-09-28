import os

from programy.clients.events.console.client import ConsoleBotClient
from programy.utils.text.dateformat import DateFormatter

class ProgramYChatbot(ConsoleBotClient):
    '''
        Custom một chatbot con, giao diện Console 
    
    '''
    def __init__(self, argument_parser=None):
        ConsoleBotClient.__init__(self, argument_parser)
 
    def parse_configuration(self):
        '''
            Thiết đặt mục config liên quan đến load file aiml
        '''
        self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._files = \
            [os.path.dirname(__file__)]

    def add_local_properties(self):
        '''
            Bổ sung các props riêng có của chatbot này
        '''
        client_context = self.create_client_context("console")
        client_context.brain.properties.add_property("name", "ProgramY")
        client_context.brain.properties.add_property("app_version", "1.0.0")
        client_context.brain.properties.add_property("grammar_version", "1.0.0")
        date_formatter = DateFormatter()
        client_context.brain.properties.add_property("birthdate", date_formatter.locate_appropriate_date_time())

if __name__ == '__main__':

    print ("Running ProgramY Chatbot with default options....")

    chatbot = ProgramYChatbot()

    chatbot.add_local_properties()

    chatbot.run()


