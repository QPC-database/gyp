{
  'variables': {
    'depth': '..',
  },
  'includes': [
    '../build/common.gypi',
    '../build/external_code.gypi',
  ],
  'target_defaults': {
    'include_dirs': [
      '..',
    ],
    'defines': [
      ['BUILDING_CHROMIUM__', 1],
      ['ENABLE_DATABASE', 1],
      ['ENABLE_DASHBOARD_SUPPORT', 0],
      ['ENABLE_JAVASCRIPT_DEBUGGER', 0],
      ['ENABLE_JSC_MULTIPLE_THREADS', 0],
      ['ENABLE_ICONDATABASE', 0],
      ['ENABLE_XSLT', 1],
      ['ENABLE_XPATH', 1],
      ['ENABLE_SVG', 1],
      ['ENABLE_SVG_ANIMATION', 1],
      ['ENABLE_SVG_AS_IMAGE', 1],
      ['ENABLE_SVG_USE', 1],
      ['ENABLE_SVG_FOREIGN_OBJECT', 1],
      ['ENABLE_SVG_FONTS', 1],
      ['ENABLE_VIDEO', 1],
      ['ENABLE_WORKERS', 0],
      ['USE_GOOGLE_URL_LIBRARY', 1],
      ['USE_SYSTEM_MALLOC', 1],
    ],
    'conditions': [
      ['OS=="mac"', {
        'defines': [
          ['WEBCORE_NAVIGATOR_PLATFORM_', '"FixMeAndRemoveTrailingUnderscore"'],
        ],
      }],
      ['OS=="win"', {
        'defines': [
          ['CRASH', '__debugbreak'],
          ['WEBCORE_NAVIGATOR_PLATFORM', '"Win32"'],
        ],
      }],
    ],
    'sources/': [
      ['exclude', '(Mac|Win|Pthreads)\\.(cpp|mm)$'],
    ],
    'conditions': [
      ['OS=="mac"', {'sources/': [['include', '(Mac|Pthreads)\\.(cpp|mm)$']]}],
      ['OS=="win"', {'sources/': [['include', 'Win\\.cpp$']]}],
    ],
  },
  'targets': [
    {
      'target_name': 'wtf',
      'type': 'static_library',
      'dependencies': [
        '../third_party/icu38/icu38.gyp:icui18n',
        '../third_party/icu38/icu38.gyp:icuuc',
      ],
      'include_dirs': [
        '../third_party/WebKit/JavaScriptCore',
        '../third_party/WebKit/JavaScriptCore/wtf',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode',
      ],
      'sources': [
        '../third_party/WebKit/JavaScriptCore/wtf/chromium/ChromiumThreading.h',
        '../third_party/WebKit/JavaScriptCore/wtf/chromium/MainThreadChromium.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/gtk/MainThreadGtk.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/mac/MainThreadMac.mm',
        #'../third_party/WebKit/JavaScriptCore/wtf/qt/MainThreadQt.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/icu/CollatorICU.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/icu/UnicodeIcu.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/unicode/qt4/UnicodeQt4.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/Collator.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/unicode/CollatorDefault.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/Unicode.h',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/UTF8.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/unicode/UTF8.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/win/MainThreadWin.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/wx/MainThreadWx.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/AlwaysInline.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ASCIICType.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Assertions.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/Assertions.h',
        '../third_party/WebKit/JavaScriptCore/wtf/AVLTree.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ByteArray.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/ByteArray.h',
        '../third_party/WebKit/JavaScriptCore/wtf/CurrentTime.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/CurrentTime.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Deque.h',
        '../third_party/WebKit/JavaScriptCore/wtf/dtoa.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/dtoa.h',
        '../third_party/WebKit/JavaScriptCore/wtf/FastMalloc.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/FastMalloc.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Forward.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/GOwnPtr.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/GOwnPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/GetPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashCountedSet.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashFunctions.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashIterators.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashMap.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashSet.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashTable.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/HashTable.h',
        '../third_party/WebKit/JavaScriptCore/wtf/HashTraits.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ListHashSet.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ListRefPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Locker.h',
        '../third_party/WebKit/JavaScriptCore/wtf/MainThread.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/MainThread.h',
        '../third_party/WebKit/JavaScriptCore/wtf/MallocZoneSupport.h',
        '../third_party/WebKit/JavaScriptCore/wtf/MathExtras.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Noncopyable.h',
        '../third_party/WebKit/JavaScriptCore/wtf/NotFound.h',
        '../third_party/WebKit/JavaScriptCore/wtf/OwnArrayPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/OwnPtr.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/OwnPtrWin.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/PassRefPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Platform.h',
        '../third_party/WebKit/JavaScriptCore/wtf/PtrAndFlags.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RandomNumber.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/RandomNumber.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RandomNumberSeed.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RefCounted.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RefCountedLeakCounter.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/RefCountedLeakCounter.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RefPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RefPtrHashMap.h',
        '../third_party/WebKit/JavaScriptCore/wtf/RetainPtr.h',
        '../third_party/WebKit/JavaScriptCore/wtf/StdLibExtras.h',
        '../third_party/WebKit/JavaScriptCore/wtf/StringExtras.h',
        '../third_party/WebKit/JavaScriptCore/wtf/TCPackedCache.h',
        '../third_party/WebKit/JavaScriptCore/wtf/TCPageMap.h',
        '../third_party/WebKit/JavaScriptCore/wtf/TCSpinLock.h',
        '../third_party/WebKit/JavaScriptCore/wtf/TCSystemAlloc.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/TCSystemAlloc.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Threading.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/Threading.h',
        #'../third_party/WebKit/JavaScriptCore/wtf/ThreadingGtk.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/ThreadingNone.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/ThreadingPthreads.cpp',
        #'../third_party/WebKit/JavaScriptCore/wtf/ThreadingQt.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/ThreadingWin.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/ThreadSpecific.h',
        '../third_party/WebKit/JavaScriptCore/wtf/ThreadSpecificWin.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/TypeTraits.cpp',
        '../third_party/WebKit/JavaScriptCore/wtf/TypeTraits.h',
        '../third_party/WebKit/JavaScriptCore/wtf/UnusedParam.h',
        '../third_party/WebKit/JavaScriptCore/wtf/Vector.h',
        '../third_party/WebKit/JavaScriptCore/wtf/VectorTraits.h',
        'build/precompiled_webkit.cc',
        'build/precompiled_webkit.h',
      ],
      'conditions': [
        ['OS=="win"', {
          'defines': [
            '__STD_C',
            '_SCL_SECURE_NO_DEPRECATE',
            '_CRT_SECURE_NO_DEPRECATE',
          ],
          'include_dirs': [
            'build/JavaScriptCore',
            '../third_party/WebKit/JavaScriptCore/os-win32',
          ],
          'msvs_precompiled_header': 'build/precompiled_webkit.h',
          'msvs_precompiled_source': 'build/precompiled_webkit.cc',
          'configurations': {
            'Debug': {
              'msvs_precompiled_headers_enabled': 1,
            },
            'Release': {
              'msvs_precompiled_headers_enabled': 0,
            },
          },
        }, {
            'sources!': [
              'build/precompiled_webkit.h',
              'build/precompiled_webkit.cc',
            ],
        },],
      ],
      'msvs_disabled_warnings': [4127, 4355, 4510, 4512, 4610, 4706],
    },
    {
      'target_name': 'v8bindings',
      'type': 'static_library',
      'dependencies': [
        'wtf',
      ],
      'rules': [
        {
          'rule_name': 'bison',
          'extension': 'y',
          'outputs': [
            '<(INTERMEDIATE_DIR)/*.cpp',
            '<(INTERMEDIATE_DIR)/*.h'
          ],
          'action': 'python rule_bison.py * <(INTERMEDIATE_DIR)',
          'process_outputs_as_sources': 'yes',
        }
      ],
      'sources': [
        '../third_party/WebKit/WebCore/css/CSSGrammar.y',
        '../third_party/WebKit/WebCore/xml/XPathGrammar.y',
      ],
    },
  ],
  'conditions': [
    ['OS=="win"', {
      'targets': [
        {
          'target_name': 'webkit_resources',
          'type': 'none',
          'sources': [
            'glue/webkit_resources.grd',
          ],
          'msvs_tool_files': ['../tools/grit/build/grit_resources.rules'],
          'direct_dependent_settings': {
            'include_dirs': [
              '$(OutDir)/grit_derived_sources',
            ],
          },
        },
      ],
    }],
  ],
}