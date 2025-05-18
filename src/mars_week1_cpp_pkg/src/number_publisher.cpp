#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

class NumberPublisher : public rclcpp::Node {
public:
    NumberPublisher() : Node("number_publisher") {
        publisher_ = this->create_publisher<std_msgs::msg::Int32>("number", 10);
        timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&NumberPublisher::publish_number, this));
        number_ = 1;
    }

private:
    void publish_number() {
        auto msg = std_msgs::msg::Int32();
        msg.data = number_;
        RCLCPP_INFO(this->get_logger(), "Publishing: %d", msg.data);
        publisher_->publish(msg);
        number_++;
    }

    rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    int number_;
};

int main(int argc, char *argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<NumberPublisher>());
    rclcpp::shutdown();
    return 0;
}

