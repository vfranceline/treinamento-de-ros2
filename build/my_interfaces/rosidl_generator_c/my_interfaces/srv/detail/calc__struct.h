// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_interfaces:srv/Calc.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__CALC__STRUCT_H_
#define MY_INTERFACES__SRV__DETAIL__CALC__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'op'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Calc in the package my_interfaces.
typedef struct my_interfaces__srv__Calc_Request
{
  double a;
  double b;
  rosidl_runtime_c__String op;
} my_interfaces__srv__Calc_Request;

// Struct for a sequence of my_interfaces__srv__Calc_Request.
typedef struct my_interfaces__srv__Calc_Request__Sequence
{
  my_interfaces__srv__Calc_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Calc_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'status'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Calc in the package my_interfaces.
typedef struct my_interfaces__srv__Calc_Response
{
  double resultado;
  rosidl_runtime_c__String status;
} my_interfaces__srv__Calc_Response;

// Struct for a sequence of my_interfaces__srv__Calc_Response.
typedef struct my_interfaces__srv__Calc_Response__Sequence
{
  my_interfaces__srv__Calc_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Calc_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_INTERFACES__SRV__DETAIL__CALC__STRUCT_H_
