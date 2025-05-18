#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

class SquareSubscriber : public rclcpp::Node {
public:
    SquareSubscriber() : Node("square_subscriber") {
        subscription_ = this->create_subscription<std_msgs::msg::Int32>(
            "number", 10,
            std::bind(&SquareSubscriber::callback, this, std::placeholders::_1)
        );
    }

private:
    void callback(const std_msgs::msg::Int32::SharedPtr msg) {
        int square = msg->data * msg->data;
        RCLCPP_INFO(this->get_logger(), "Received: %d | Square: %d", msg->data, square);
    }

    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr subscription_;
};

int main(int argc, char *argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<SquareSubscriber>());
    rclcpp::shutdown();
    return 0;
}

