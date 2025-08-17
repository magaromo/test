print("hello")


# Example of a function that checks the gate mode and returns the corresponding path
def get_path_for_gate_mode(self, response):
    if self.gate_mode not in self.modes:
        self.get_logger().error(f"Invalid gate mode: {self.gate_mode}")
        response.success = False
        response.message = f"Invalid gate mode: {self.gate_mode}"
        return response

    self.get_logger().info(f"Valid gate mode: {self.gate_mode}")
    index = self.modes.index(self.gate_mode)
    the_path = self.function_list[index]()
    
    return the_path