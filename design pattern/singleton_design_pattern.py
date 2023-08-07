class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        # Perform any initialization tasks here
        self.config_data = {}

    def set_config(self, key, value):
        self.config_data[key] = value

    def get_config(self, key):
        return self.config_data.get(key)

    def print_config(self):
        for key, value in self.config_data.items():
            print(f"{key}: {value}")
if __name__ == "__main__":
    config_manager1 = ConfigurationManager()
    config_manager1.set_config("LogLevel", "DEBUG")
    config_manager1.set_config("MaxConnections", 10)

    config_manager2 = ConfigurationManager()
    config_manager2.set_config("Timeout", 30)

    # Both config_manager1 and config_manager2 refer to the same instance
    print("Configuration Manager 1:")
    config_manager1.print_config()

    print("\nConfiguration Manager 2:")
    config_manager2.print_config()


#output:
#Configuration Manager 1:
#LogLevel: DEBUG
#MaxConnections: 10
#Timeout: 30

#Configuration Manager 2:
#LogLevel: DEBUG
#MaxConnections: 10
#Timeout: 30