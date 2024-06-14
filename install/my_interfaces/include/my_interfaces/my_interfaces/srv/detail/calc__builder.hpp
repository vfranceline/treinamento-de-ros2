// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:srv/Calc.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__CALC__BUILDER_HPP_
#define MY_INTERFACES__SRV__DETAIL__CALC__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/srv/detail/calc__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Calc_Request_op
{
public:
  explicit Init_Calc_Request_op(::my_interfaces::srv::Calc_Request & msg)
  : msg_(msg)
  {}
  ::my_interfaces::srv::Calc_Request op(::my_interfaces::srv::Calc_Request::_op_type arg)
  {
    msg_.op = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Calc_Request msg_;
};

class Init_Calc_Request_b
{
public:
  explicit Init_Calc_Request_b(::my_interfaces::srv::Calc_Request & msg)
  : msg_(msg)
  {}
  Init_Calc_Request_op b(::my_interfaces::srv::Calc_Request::_b_type arg)
  {
    msg_.b = std::move(arg);
    return Init_Calc_Request_op(msg_);
  }

private:
  ::my_interfaces::srv::Calc_Request msg_;
};

class Init_Calc_Request_a
{
public:
  Init_Calc_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Calc_Request_b a(::my_interfaces::srv::Calc_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_Calc_Request_b(msg_);
  }

private:
  ::my_interfaces::srv::Calc_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Calc_Request>()
{
  return my_interfaces::srv::builder::Init_Calc_Request_a();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Calc_Response_status
{
public:
  explicit Init_Calc_Response_status(::my_interfaces::srv::Calc_Response & msg)
  : msg_(msg)
  {}
  ::my_interfaces::srv::Calc_Response status(::my_interfaces::srv::Calc_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Calc_Response msg_;
};

class Init_Calc_Response_resultado
{
public:
  Init_Calc_Response_resultado()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Calc_Response_status resultado(::my_interfaces::srv::Calc_Response::_resultado_type arg)
  {
    msg_.resultado = std::move(arg);
    return Init_Calc_Response_status(msg_);
  }

private:
  ::my_interfaces::srv::Calc_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Calc_Response>()
{
  return my_interfaces::srv::builder::Init_Calc_Response_resultado();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__CALC__BUILDER_HPP_
