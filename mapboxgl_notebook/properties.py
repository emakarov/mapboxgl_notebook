"""Managing Paint objects."""


class Property:

    def init_data(self, properties):
        """Initialisation of self.data from passed properties."""
        self.data = {}
        for key in properties:
            if properties[key] is not None:
                self.data[key] = properties[key]

class Layout(Property):

    def __init__(
            self,
            visibility=None,
            line_cap=None,
            line_join=None,
            line_miter_limit=None,
            line_round_limit=None,
            line_opacity=None,
            # Symbol
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-symbol
            symbol_placement=None,
            symbol_spacing=None,
            symbol_avoid_edges=None,
            symbol_z_order=None,
            icon_allow_overlap=None,
            icon_ignore_placement=None,
            icon_optional=None,
            icon_rotation_alignment=None,
            icon_size=None,
            icon_text_fit=None,
            icon_text_fit_padding=None,
            icon_image=None,
            icon_rotate=None,
            icon_padding=None,
            icon_keep_upright=None,
            icon_offset=None,
            icon_anchor=None,
            icon_pitch_alignment=None,
            text_pitch_alignment=None,
            text_rotation_alignment=None,
            text_field=None,
            text_font=None,
            text_size=None,
            text_max_width=None,
            text_line_height=None,
            text_letter_spacing=None,
            text_justify=None,
            text_anchor=None,
            text_max_angle=None,
            text_rotate=None,
            text_padding=None,
            text_keep_upright=None,
            text_transform=None,
            text_offset=None,
            text_allow_overlap=None,
            text_ignore_placement=None,
            text_optional=None,

        ):
        properties = {
            'visibility': visibility,
            # Line https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-line
            'line-cap': line_cap,
            'line-join': line_join,
            'line-miter-limit': line_miter_limit,
            'line-round-limit': line_round_limit,
            'line-opacity': line_opacity,
            # Symbol
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-symbol
            'symbol-placement': symbol_placement,
            'symbol-spacing': symbol_spacing,
            'symbol-avoid-edges': symbol_avoid_edges,
            'symbol-z-order': symbol_z_order,
            'icon-allow-overlap': icon_allow_overlap,
            'icon-ignore-placement': icon_ignore_placement,
            'icon-optional': icon_optional,
            'icon-rotation-alignment': icon_rotation_alignment,
            'icon-size': icon_size,
            'icon-text-fit': icon_text_fit,
            'icon-text-fit-padding': icon_text_fit_padding,
            'icon-image': icon_image,
            'icon-rotate': icon_rotate,
            'icon-padding': icon_padding,
            'icon-keep-upright': icon_keep_upright,
            'icon-offset': icon_offset,
            'icon-anchor': icon_anchor,
            'icon-pitch-alignment': icon_pitch_alignment,
            'text-pitch-alignment': text_pitch_alignment,
            'text-rotation-alignment': text_rotation_alignment,
            'text-field': text_field,
            'text-font': text_font,
            'text-size': text_size,
            'text-max-width': text_max_width,
            'text-line-height': text_line_height,
            'text-letter-spacing': text_letter_spacing,
            'text-justify': text_justify,
            'text-anchor': text_anchor,
            'text-max-angle': text_max_angle,
            'text-rotate': text_rotate,
            'text-padding': text_padding,
            'text-keep-upright': text_keep_upright,
            'text-transform': text_transform,
            'text-offset': text_offset,
            'text-allow-overlap': text_allow_overlap,
            'text-ignore-placement': text_ignore_placement,
            'text-optional': text_optional,

        }
        self.init_data(properties)


class Paint(Property):
    """
    Paint layer object
    """

    def __init__(
            self,
            # background properties
            # See https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-background
            background_color=None,
            background_pattern=None,
            background_opacity=None,
            # Fill properties
            # See https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-fill
            fill_antialias=None,
            fill_opacity=None,
            fill_color=None,
            fill_outline_color=None,
            fill_translate=None,
            fill_translate_anchor=None,
            fill_pattern=None,
            # Line https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-line
            line_color=None,
            line_translate=None,
            line_translate_anchor=None,
            line_width=None,
            line_gap_width=None,
            line_offset=None,
            line_blur=None,
            line_dasharray=None,
            line_pattern=None,
            line_gradient=None,
            # Symbol
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-symbol
            icon_opacity=None,
            icon_color=None,
            icon_halo_color=None,
            icon_halo_width=None,
            icon_halo_blur=None,
            icon_translate=None,
            icon_translate_anchor=None,
            text_opacity=None,
            text_color=None,
            text_halo_color=None,
            text_halo_width=None,
            text_halo_blur=None,
            text_translate=None,
            text_translate_anchor=None,
            # Raster
            raster_opacity=None,
            raster_hue_rotate=None,
            raster_brightness_min=None,
            raster_brightness_max=None,
            raster_saturation=None,
            raster_contrast=None,
            raster_resampling=None,
            raster_fade_duration=None,
            # Circle
            circle_radius=None,
            circle_color=None,
            circle_blur=None,
            circle_opacity=None,
            circle_translate=None,
            circle_translate_anchor=None,
            circle_pitch_scale=None,
            circle_pitch_alignment=None,
            circle_stroke_width=None,
            circle_stroke_color=None,
            circle_stroke_opacity=None,
            # FIll extrusion
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-fill-extrusion
            fill_extrusion_opacity=None,
            fill_extrusion_color=None,
            fill_extrusion_translate=None,
            fill_extrusion_translate_anchor=None,
            fill_extrusion_pattern=None,
            fill_extrusion_height=None,
            fill_extrusion_base=None,
            fill_extrusion_vertical_gradient=None,
            # Heatmap
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-heatmap
            heatmap_radius=None,
            heatmap_weight=None,
            heatmap_intensity=None,
            heatmap_color=None,
            heatmap_opacity=None,
            # Hillshade
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-hillshade
            hillshade_illumination_direction=None,
            hillshade_illumination_anchor=None,
            hillshade_exaggeration=None,
            hillshade_shadow_color=None,
            hillshade_highlight_color=None,
            hillshade_accent_color=None,
        ):
        properties = {
            # background
            'background-color': background_color,
            'background-pattern': background_pattern,
            'background-opacity': background_opacity,

            # fill
            # See https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-fill
            'fill-antialias': fill_antialias,
            'fill-opacity': fill_opacity,
            'fill-color': fill_color,
            'fill-outline-color': fill_outline_color,
            'fill-translate': fill_translate,
            'fill-translate-anchor': fill_translate_anchor,
            'fill-pattern': fill_pattern,

            # line https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-line
            'line-color': line_color,
            'line-translate': line_translate,
            'line-translate-anchor': line_translate_anchor,
            'line-width': line_width,
            'line-gap-width': line_gap_width,
            'line-offset': line_offset,
            'line-blur': line_blur,
            'line-dasharray': line_dasharray,
            'line-pattern': line_pattern,
            'line-gradient': line_gradient,
            # Symbol
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-symbol
            'icon-opacity': icon_opacity,
            'icon-color': icon_color,
            'icon-halo-color': icon_halo_color,
            'icon-halo-width': icon_halo_width,
            'icon-halo-blur': icon_halo_blur,
            'icon-translate': icon_translate,
            'icon-translate-anchor': icon_translate_anchor,
            'text-opacity': text_opacity,
            'text-color': text_color,
            'text-halo-color': text_halo_color,
            'text-halo-width': text_halo_width,
            'text-halo-blur': text_halo_blur,
            'text-translate': text_translate,
            'text-translate-anchor': text_translate_anchor,
            # Raster
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-raster
            'raster-opacity': raster_opacity,
            'raster-hue-rotate': raster_hue_rotate,
            'raster-brightness-min': raster_brightness_min,
            'raster-brightness-max': raster_brightness_max,
            'raster-saturation': raster_saturation,
            'raster-contrast': raster_contrast,
            'raster-resampling': raster_resampling,
            'raster-fade-duration': raster_fade_duration,
            # Circle
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-circle
            'circle-radius': circle_radius,
            'circle-color': circle_color,
            'circle-blur': circle_blur,
            'circle-opacity': circle_opacity,
            'circle-translate': circle_translate,
            'circle-translate-anchor': circle_translate_anchor,
            'circle-pitch-scale': circle_pitch_scale,
            'circle-pitch-alignment': circle_pitch_alignment,
            'circle-stroke-width': circle_stroke_width,
            'circle-stroke-color': circle_stroke_color,
            'circle-stroke-opacity': circle_stroke_opacity,
            # FIll extrusion
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-fill-extrusion
            'fill-extrusion-opacity': fill_extrusion_opacity,
            'fill-extrusion-color': fill_extrusion_color,
            'fill-extrusion-translate': fill_extrusion_translate,
            'fill-extrusion-translate-anchor': fill_extrusion_translate_anchor,
            'fill-extrusion-pattern': fill_extrusion_pattern,
            'fill-extrusion-height': fill_extrusion_height,
            'fill-extrusion-base': fill_extrusion_base,
            'fill-extrusion-vertical-gradient': fill_extrusion_vertical_gradient,
            # Heatmap
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-heatmap
            'heatmap-radius': heatmap_radius,
            'heatmap-weight': heatmap_weight,
            'heatmap-intensity': heatmap_intensity,
            'heatmap-color': heatmap_color,
            'heatmap-opacity': heatmap_opacity,
            # Hillshade
            # https://docs.mapbox.com/mapbox-gl-js/style-spec#layers-hillshade
            'hillshade-illumination-direction': hillshade_illumination_direction,
            'hillshade-illumination-anchor': hillshade_illumination_anchor,
            'hillshade-exaggeration': hillshade_exaggeration,
            'hillshade-shadow-color': hillshade_shadow_color,
            'hillshade-highlight-color': hillshade_highlight_color,
            'hillshade-accent-color': hillshade_accent_color
        }
        self.init_data(properties)
