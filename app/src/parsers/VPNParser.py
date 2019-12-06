import xml.etree.ElementTree as et
from os import listdir, chdir
from persons.models import Person


class VPNParser:
    """
    Class that reads logs of the VPN and stores it in the database.
    """

    @staticmethod
    def __get_user(user_login):
        """
        Gets the user from the database.

        Returns
        -------
        int
            an int that identifies a person
        """
        identifier = None
        try:
            identifier = Person.objects.get(login=user_login).id
        except DoesNotExist:
            print(f'User not found for login {user_login}!')
        finally:
            return identifier

    @staticmethod
    def __check_directory():
        """
        Checks if there are VPN XML files to parse and returns a list with the names

        Returns
        -------
        list
            a list with all the names of the XML files
        """
        return listdir('..\\log_examples\\vpn_logs')

    def load_data(self):  # TODO - Finish
        """
        Loads the VPN XML log in memory.

        Returns
        -------
        ndarray
            an array with the event, app (Windows OS), person id, item id and timestamps
        """
        files = self.__check_directory()
        roots = [et.parse(f'../log_examples/vpn_logs/{file}').getroot() for file in files]

        for root in roots[0]:
            for summary in root.findall('Summary'):
                print(summary.findtext('Hora')) # Timestamp
                print(summary.findtext('IPdeliniciador')) # IP
                print(summary.findtext('Usuario')) # Person
                print(summary.findtext('Duración')) # Time
                print(summary.findtext('Servicio')) # App
                print(summary.findtext('Mensaje')) # EventType

    def __store_data(self):  # TODO
        """
        Stores the data into the Event entity and Passage entity.
        """
        pass

    def parse(self):  # TODO
        """
        Parses the events of the VPN and stores them in the database.
        """
        pass
