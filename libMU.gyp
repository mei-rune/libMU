{
  'variables': {
    'YAJL_MAJOR': '2',
    'YAJL_MINOR': '0',
    'YAJL_MICRO': '5',
  },
  'targets': [
    {
      'target_name': 'libMU',
      'type': 'static_library',
      'sources': [
          'src/atomic.c',
          'src/hashtable.c',
          'src/itostr.c',
          'src/json_tokener.c',
          'src/networking.c',
          'src/object.c',
          'src/object_array.c',
          'src/object_format.c',
          'src/object_new.c',
          'src/object_string.c',
          'src/object_table.c',
          'src/object_to.c',
          'src/object_utils.c',
          'src/rollingfile.c',
          'src/string_buffer.c',
          'src/target.c',
          'src/unittest.c',
          'src/url.c',
          'src/utils.c',
          'src/win32/dirent.c',
          'src/win32/dlfcn.c',
          'src/win32/getopt.c',
          'src/win32/getopt1.c',
          'src/win32/gettimeofday.c',
          'src/win32/iputilities.c',
          'src/win32/pthread_windows.c',
          'src/win32/sem.c',
          'src/json/json.c',
          'src/json/json_array.c',
          'src/json/json_mapping.c',
          'src/json/json_number.c',
          'src/json/json_string.c',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)',
        ]
      },
      'include_dirs': [
        'src',
        'include',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      'defines': [ 'NETSNMP_ENABLE_IPV6' ],
      'conditions': [
        ['OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"', {
          'cflags': [ '--std=c89' ],
          'defines': [ '_GNU_SOURCE' ]
        }],
        ['OS=="win32"', {
          'defines': [ 'HAVE_WIN32_PLATFORM_SDK' ]
        }],
      ],
    }, # end libMU
    {
      'target_name': 'libMU_test',
      'type': 'executable',
      'dependencies': [
        'libMU',
      ],
      'sources': [
          'test/array_test.c',
          'test/hashtable_test.c',
          'test/json_test.c',
          'test/object_test.c',
          'test/main.c',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)',
        ]
      },
      'include_dirs': [
        'test',
        'include',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      'defines': [ 'NETSNMP_ENABLE_IPV6' ],
       'conditions': [
        ['OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"', {
          'cflags': [ '--std=c89' ],
          'defines': [ '_GNU_SOURCE' ]
        }],
        ['OS=="win32"', {
          'defines': [ 'HAVE_WIN32_PLATFORM_SDK' ]
        }],
      ],
    }, # end libMU_test
  ] # end targets
}
