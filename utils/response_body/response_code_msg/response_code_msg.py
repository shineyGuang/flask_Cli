#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2021/2/19 17:53
# @Site    :
# @File    : response_code_msg.py
# @Software: PyCharm
"""



class ResponseCode(object):
    Success = 200  # 成功
    CreateSuccess = 201  # 创建成功
    DeleteSuccess = 204  # 删除成功
    Fail = 500  # 失败
    NoResourceFound = 404  # 未找到资源
    InvalidParameter = 400  # 错误的请求
    Forbidden = 403  # 禁止访问
    ExpectationFailed = 417  # 请求头错误
    UnprocessableEntity = 422  # 请求content-type错误
    AuthFailed = 401  # 身份验证失败，需要登录

    FlushTokenCode = 777


class ResponseMessage(object):
    FormTagMakeErr = "Form表单生成失败"
    EnumTypeErr = "枚举类型错误"
    LoginSuccess = "登录成功"
    Success = "成功"
    DeleteSuccess = "删除成功"
    DeleteFail = "删除失败"
    Fail = "失败"
    NoResourceFound = "未找到资源"
    InvalidParameter = "参数无效"
    NotFondUserErr = "用户不存在"
    NotFondResourceErr = "数据库未找到资源"
    PasswordErr = "用户密码错误"
    IllegalLoginErr = "非法登录,请选择正确登录方式"
    # Token
    TokeninvalidErr = "传入无效的token,验证身份失败"
    TokenTimeOutErr = "token超时,请重新登录"
    TokenFlushSuccess = "刷新token成功"

    # 接口
    NoPermissionApiErr = "您没有权限访问该接口"
    InterfaceIsExistsErr = "当前接口已被占用,请更换"
    CreateInterfaceSuccess = "创建接口成功"
    InterfaceIsNotExistsErr = "当前接口不存在,请更换"
    EditInterfaceFail = "更改接口信息失败"
    EditInterfaceSuccess = "更改接口信息成功"
    DeleteInterfaceNotExists = "要删除的接口不存在"
    # 菜单
    MenuNameIsExistsErr = "菜单路由名称已被占用"
    MenuRouteIsExistsErr = "菜单路由路径已被占用"
    CreateMenuSuccess = "创建菜单成功"
    MenuParentIdIsNotExistsErr = "父菜单不存在"
    EditMenuFail = "更改菜单信息失败"
    EditMenuSuccess = "更改菜单信息成功"
    # 角色
    EditRoleFail = "更改角色信息失败"
    EditRoleSuccess = "更改角色信息成功"
    RoleParentIdIsNotExistsErr = "父角色id不存在"
    RoleIdIsNotExistsErr = "角色id不存在"
    RoleIdIsExistsErr = "角色id被占用,请更换"
    CreateRoleSuccess = "创建角色成功"
    GetRoleSuccess = "获取角色成功"
    CurrentRoleIsNotExistsErr = "当前角色不存在"
    # 数据
    DataRoleIsNotExistsErr = "当前角色没有分配数据权限"
    # 用户
    UserIdExistsErr = "工号重复注册"
    UserIsExistsErr = "用户名重复注册"
    PhoneIsExistsErr = "手机号重复注册"
    EmailIsExistsErr = "邮箱号重复注册"
    IdentityCodeIsExistsErr = "身份证号重复注册"
    CreateUserFail = "创建用户失败"
    UserRepeatLoginErr = "当前用户在其他地方登陆，请重新登陆"
    RobotNameIsExistsErr = "当前注册机器人已存在"
    # 设备
    EquipmentRegisterSuccess = "当前设备注册信息成功"
    ExistDeleteErr = "当前有{}条数据无法删除，这些数据下已存在绑定关系。"
    EquimentTypeIsUseErr = "当前设备类型已被使用"
    EquimentTypeNotFond = "没有找到该设备类型"
    EquimentTypeErr = "当前设备类型没有查询到"
    EquimentIsUseErr = "当前设备的【设备序列号】已经被使用"
    AddEquimentSuccess = "添加设备成功"
    AddEquimentTypeSuccess = "添加设备类型成功"
    NotFoundTypeGroupsErr = "获取分组类型失败"
    EquimentNotFond = "没有找到该设备"
    EquipemtNotMathTrainSys = "当前设备没有匹配到训练系统"
    EquipmentWriteBitesErr = "写入数据失败"
    # 训练系统
    AddTrainSysProgramSuccess = "创建训练系统成功"
    TrainSysProgramNameIsUseErr = "训练系统名称已经存在"
    TrainSysProgramNameErr = "训练系统名称不能为空"
    TrainSysProgramBindErr = "最大绑定设备不能为空"
    TrainSysProgramTimeErr = "训练时长不能为空"
    TrainSysProgramIsUseErr = "当前训练系统的【训练名称】已经被使用"
    TrainSysProgramBindOverMaxErr = "当前训练系统绑定设备数量大于设置数量"
    TrainSysProgramNameNotExistErr = "训练系统不存在"
    BindEquipmentSuccess = "绑定设备成功"
    BindEquipmentErr = "绑定设备失败"
    UnBindBindEquipmentNotExistsErr = "要解绑的设备不存在"
    UnBindBindEquipmentSuccess = "解绑设备成功"
    UnBindBindEquipmentErr = "解绑设备失败"
    BindEquipmentNotFound = "当前训练系统下没有找到绑定设备"
    CurrentSystemIsNotNetwork = "当前训练系统无法连接网络"

