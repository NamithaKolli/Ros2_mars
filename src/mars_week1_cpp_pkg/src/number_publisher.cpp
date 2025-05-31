#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

class NumberPublisher : public rclcpp::Node {
public:
    NumberPublisher() : Node("number_publisher") {
        // Define a custom QoS profile
        rclcpp::QoS qos_profile(rclcpp::QoSInitialization::from_rmw(rmw_qos_profile_default));
        qos_profile.reliability(RMW_QOS_POLICY_RELIABILITY_RELIABLE);
        qos_profile.durability(RMW_QOS_POLICY_DURABILITY_VOLATILE);
        qos_profile.history(RMW_QOS_POLICY_HISTORY_KEEP_LAST).keep_last(10);

        // Create publisher with the QoS profile
        publisher_ = this->create_publisher<std_msgs::msg::Int32>("number", qos_profile);

        timer_ = this->create_wall_timer(
            std::chrono::seconds(1),
            std::bind(&NumberPublisher::publish_number, this)
        );

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

