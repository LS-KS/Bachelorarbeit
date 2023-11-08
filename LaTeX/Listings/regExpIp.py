def __validateIP(self, ip):
        """
        This method validates the entered IP string
        and returns True if valid

        :param ip:
        :type ip: str
        :return: boolean
        """
        if ip == "":
            return False
        elif ip == None:
            return False
        ip = ip.split(".")
        if len(ip) != 4:
            return False
        for idx, i in enumerate(ip):
            if not isinstance(int(i), int):
                return False
            else:
                if int(i) < 0 or int(i) > 255:
                    return False
            if idx == 0:
                if int(i) < 127:
                    return False
        return True