INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TRIGGER trigger)

FIND_PATH(
    TRIGGER_INCLUDE_DIRS
    NAMES trigger/api.h
    HINTS $ENV{TRIGGER_DIR}/include
        ${PC_TRIGGER_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TRIGGER_LIBRARIES
    NAMES gnuradio-trigger
    HINTS $ENV{TRIGGER_DIR}/lib
        ${PC_TRIGGER_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TRIGGER DEFAULT_MSG TRIGGER_LIBRARIES TRIGGER_INCLUDE_DIRS)
MARK_AS_ADVANCED(TRIGGER_LIBRARIES TRIGGER_INCLUDE_DIRS)

