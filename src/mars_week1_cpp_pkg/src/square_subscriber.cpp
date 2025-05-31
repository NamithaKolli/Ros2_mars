#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

class SquareSubscriber : public rclcpp::Node {
public:
    SquareSubscriber() : Node("square_subscriber") {
        // Define a custom QoS profile
        rclcpp::QoS qos_profile(rclcpp::QoSInitialization::from_rmw(rmw_qos_profile_default));
        qos_profile.reliability(RMW_QOS_POLICY_RELIABILITY_RELIABLE);
        qos_profile.durability(RMW_QOS_POLICY_DURABILITY_VOLATILE);
        qos_profile.history(RMW_QOS_POLICY_HISTORY_KEEP_LAST).keep_last(10);

        // Create subscription with the QoS profile
        subscription_ = this->create_subscription<std_msgs::msg::Int32>(
            "number", qos_profile,
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

