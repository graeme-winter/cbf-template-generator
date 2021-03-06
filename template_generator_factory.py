from __future__ import division, print_function

def template_generator_factory(beamline, data_collection_info):

  if beamline == 'ixx':
    from dls_template_generator import dls_template_generator
    return dls_template_generator(beamline, data_collection_info)

  if beamline == 'i04':
    from i04_template_generator import i04_template_generator
    return i04_template_generator(beamline, data_collection_info)

  if beamline == 'i19-1':
    from i19_1_template_generator import i19_1_template_generator
    return i19_1_template_generator(beamline, data_collection_info)

  if beamline == 'i19-2':
    from i19_2_template_generator import i19_2_template_generator
    return i19_2_template_generator(beamline, data_collection_info)

if __name__ == '__main__':
  # this illustrates what we are expecting to be passed...
  example_dc_info = {'detector':{'distance_mm':187.5,
                                 'beam_x_pixel':1234.5,
                                 'beam_y_pixel':1024.0},
                     'beam':{}}

  import sys
  generator = template_generator_factory(sys.argv[1], example_dc_info)
  print(generator())
