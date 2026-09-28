<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" simplifyDrawingHints="1" simplifyLocal="1" labelsEnabled="0" simplifyAlgorithm="0" simplifyDrawingTol="1" styleCategories="AllStyleCategories" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" minScale="1e+08" version="3.10.11-A Coruña" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" type="categorizedSymbol" enableorderby="0" attr="kodKarto250k" symbollevels="1">
    <categories>
      <category label="woda powierzchniowa" symbol="0" render="true" value="0250_603"/>
      <category label="rzeka zeglowna w skali" symbol="1" render="true" value="0250_607_1"/>
      <category label="rzeka niezeglowna w skali" symbol="2" render="true" value="0250_608_1"/>
    </categories>
    <symbols>
      <symbol alpha="1" name="0" type="fill" clip_to_extent="1" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="217,239,250,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MapUnit" k="offset_unit"/>
          <prop v="83,174,221,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="40" k="outline_width"/>
          <prop v="MapUnit" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="1" type="fill" clip_to_extent="1" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="217,239,250,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MapUnit" k="offset_unit"/>
          <prop v="0,106,167,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="40" k="outline_width"/>
          <prop v="MapUnit" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="2" type="fill" clip_to_extent="1" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="217,239,250,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MapUnit" k="offset_unit"/>
          <prop v="83,174,221,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="40" k="outline_width"/>
          <prop v="MapUnit" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol alpha="1" name="0" type="fill" clip_to_extent="1" force_rhr="0">
        <layer class="SimpleFill" enabled="1" locked="0" pass="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="210,239,250,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </source-symbol>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{218570d5-d4c1-4e59-b6c6-e2578cbc4eb6}">
      <rule filter=" &quot;x_kodKarto250k&quot;  = '0250_602' and  &quot;PL.PZGiK.201.32__OT_ZBIORNIKWODNY OT_ZbiornikWodny_nazwa&quot;  &lt;> 'Morze Bałtyckie'" key="{39b63f1f-7f54-480a-8bc2-327bbe4c6dab}" description="Powierzchnia morza">
        <settings calloutType="simple">
          <text-style multilineHeight="1" fieldName="PL.PZGiK.201.32__OT_ZBIORNIKWODNY OT_ZbiornikWodny_nazwa" fontCapitals="0" useSubstitutions="0" fontSize="600" textOrientation="horizontal" fontUnderline="0" fontWeight="50" fontKerning="1" textColor="17,150,206,255" blendMode="0" fontWordSpacing="0" namedStyle="Italic" fontFamily="Cambria" fontItalic="1" fontStrikeout="0" isExpression="0" fontSizeUnit="MapUnit" previewBkgrdColor="255,255,255,255" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0.5" textOpacity="1">
            <text-buffer bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferBlendMode="0" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferNoFill="1" bufferSize="0.8" bufferJoinStyle="128"/>
            <background shapeBlendMode="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeRadiiX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeRadiiUnit="MM" shapeDraw="0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSVGFile="" shapeRotation="0" shapeSizeType="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeType="0" shapeBorderWidthUnit="MM" shapeFillColor="255,255,255,255" shapeRadiiY="0"/>
            <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowRadiusUnit="MM" shadowOpacity="0.7" shadowDraw="0" shadowScale="100" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowBlendMode="6"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format useMaxLineLengthForAutoWrap="1" formatNumbers="0" decimals="3" placeDirectionSymbol="0" wrapChar="" multilineAlign="4294967295" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" autoWrapLength="0" addDirectionSymbol="0" reverseDirectionSymbol="0" plussign="0"/>
          <placement centroidInside="0" maxCurvedCharAngleIn="25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="UnknownGeometry" distUnits="MM" geometryGeneratorEnabled="0" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" yOffset="0" offsetUnits="MM" repeatDistance="0" repeatDistanceUnits="MM" placement="4" quadOffset="4" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" overrunDistance="0" xOffset="0" placementFlags="10" priority="5" centroidWhole="0" rotationAngle="0" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" distMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" offsetType="0"/>
          <rendering scaleMax="0" upsidedownLabels="0" drawLabels="1" fontMinPixelSize="3" obstacleFactor="1" fontLimitPixelSize="0" labelPerPart="0" obstacleType="0" mergeLines="0" zIndex="0" limitNumLabels="0" scaleVisibility="0" minFeatureSize="0" displayAll="0" maxNumLabels="2000" obstacle="1" scaleMin="0" fontMaxPixelSize="10000"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
              <Option name="drawToAllParts" type="bool" value="false"/>
              <Option name="enabled" type="QString" value="0"/>
              <Option name="lineSymbol" type="QString" value="&lt;symbol alpha=&quot;1&quot; name=&quot;symbol&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option name="minLength" type="double" value="0"/>
              <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="minLengthUnit" type="QString" value="MM"/>
              <Option name="offsetFromAnchor" type="double" value="0"/>
              <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
              <Option name="offsetFromLabel" type="double" value="0"/>
              <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule filter=" &quot;x_kodKarto250k&quot;  = '0250_603'  AND  $area > 55000000" key="{b691d607-78ba-45e1-abf1-eb29845291a0}" description="Jezioro lub staw > 55mln m2">
        <settings calloutType="simple">
          <text-style multilineHeight="1" fieldName="PL.PZGiK.201.32__OT_ZBIORNIKWODNY OT_ZbiornikWodny_nazwa" fontCapitals="0" useSubstitutions="0" fontSize="800" textOrientation="horizontal" fontUnderline="0" fontWeight="50" fontKerning="1" textColor="17,150,206,255" blendMode="0" fontWordSpacing="0" namedStyle="Italic" fontFamily="Cambria" fontItalic="1" fontStrikeout="0" isExpression="0" fontSizeUnit="MapUnit" previewBkgrdColor="255,255,255,255" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0.1875" textOpacity="1">
            <text-buffer bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferBlendMode="0" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferNoFill="1" bufferSize="0.7" bufferJoinStyle="128"/>
            <background shapeBlendMode="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeRadiiX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeRadiiUnit="MM" shapeDraw="0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSVGFile="" shapeRotation="0" shapeSizeType="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeType="0" shapeBorderWidthUnit="MM" shapeFillColor="255,255,255,255" shapeRadiiY="0"/>
            <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowRadiusUnit="MM" shadowOpacity="0.7" shadowDraw="0" shadowScale="100" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowBlendMode="6"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format useMaxLineLengthForAutoWrap="1" formatNumbers="0" decimals="3" placeDirectionSymbol="0" wrapChar="" multilineAlign="4294967295" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" autoWrapLength="0" addDirectionSymbol="0" reverseDirectionSymbol="0" plussign="0"/>
          <placement centroidInside="0" maxCurvedCharAngleIn="25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="UnknownGeometry" distUnits="MM" geometryGeneratorEnabled="0" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" yOffset="0" offsetUnits="MM" repeatDistance="0" repeatDistanceUnits="MM" placement="4" quadOffset="4" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" overrunDistance="0" xOffset="0" placementFlags="10" priority="4" centroidWhole="0" rotationAngle="0" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" distMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" offsetType="0"/>
          <rendering scaleMax="0" upsidedownLabels="0" drawLabels="1" fontMinPixelSize="3" obstacleFactor="1.02" fontLimitPixelSize="0" labelPerPart="0" obstacleType="1" mergeLines="0" zIndex="0" limitNumLabels="0" scaleVisibility="0" minFeatureSize="4" displayAll="0" maxNumLabels="2000" obstacle="0" scaleMin="0" fontMaxPixelSize="10000"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
              <Option name="drawToAllParts" type="bool" value="false"/>
              <Option name="enabled" type="QString" value="0"/>
              <Option name="lineSymbol" type="QString" value="&lt;symbol alpha=&quot;1&quot; name=&quot;symbol&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option name="minLength" type="double" value="0"/>
              <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="minLengthUnit" type="QString" value="MM"/>
              <Option name="offsetFromAnchor" type="double" value="0"/>
              <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
              <Option name="offsetFromLabel" type="double" value="0"/>
              <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule filter=" &quot;x_kodKarto250k&quot;  = '0250_607_1'" key="{d1a988b6-aec5-4842-a099-bf175ff9bf77}" description="Rzeka  zeglowna w skali">
        <settings calloutType="simple">
          <text-style multilineHeight="1" fieldName="PL.PZGiK.201.32__OT_CIEK OT_Ciek_nazwa" fontCapitals="0" useSubstitutions="0" fontSize="500" textOrientation="horizontal" fontUnderline="0" fontWeight="50" fontKerning="1" textColor="17,150,206,255" blendMode="0" fontWordSpacing="0" namedStyle="Italic" fontFamily="Cambria" fontItalic="1" fontStrikeout="0" isExpression="0" fontSizeUnit="MapUnit" previewBkgrdColor="255,255,255,255" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0" textOpacity="1">
            <text-buffer bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferBlendMode="0" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferNoFill="1" bufferSize="0.7" bufferJoinStyle="128"/>
            <background shapeBlendMode="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeRadiiX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeRadiiUnit="MM" shapeDraw="0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSVGFile="" shapeRotation="0" shapeSizeType="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeType="0" shapeBorderWidthUnit="MM" shapeFillColor="255,255,255,255" shapeRadiiY="0"/>
            <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowRadiusUnit="MM" shadowOpacity="0.7" shadowDraw="0" shadowScale="100" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowBlendMode="6"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format useMaxLineLengthForAutoWrap="1" formatNumbers="0" decimals="3" placeDirectionSymbol="0" wrapChar="" multilineAlign="4294967295" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" autoWrapLength="0" addDirectionSymbol="0" reverseDirectionSymbol="0" plussign="0"/>
          <placement centroidInside="0" maxCurvedCharAngleIn="25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="UnknownGeometry" distUnits="MM" geometryGeneratorEnabled="0" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" yOffset="0" offsetUnits="MM" repeatDistance="0" repeatDistanceUnits="MM" placement="5" quadOffset="4" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" overrunDistance="0" xOffset="0" placementFlags="10" priority="5" centroidWhole="0" rotationAngle="0" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" distMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" offsetType="0"/>
          <rendering scaleMax="0" upsidedownLabels="0" drawLabels="1" fontMinPixelSize="3" obstacleFactor="1" fontLimitPixelSize="0" labelPerPart="0" obstacleType="0" mergeLines="0" zIndex="0" limitNumLabels="0" scaleVisibility="0" minFeatureSize="0" displayAll="0" maxNumLabels="2000" obstacle="1" scaleMin="0" fontMaxPixelSize="10000"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
              <Option name="drawToAllParts" type="bool" value="false"/>
              <Option name="enabled" type="QString" value="0"/>
              <Option name="lineSymbol" type="QString" value="&lt;symbol alpha=&quot;1&quot; name=&quot;symbol&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option name="minLength" type="double" value="0"/>
              <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="minLengthUnit" type="QString" value="MM"/>
              <Option name="offsetFromAnchor" type="double" value="0"/>
              <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
              <Option name="offsetFromLabel" type="double" value="0"/>
              <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule filter=" &quot;x_kodKarto250k&quot;  = '0250_608_1'" key="{16b5d157-a8c4-48de-8735-49a764c94606}" description="Rzeka niezeglownaw skali">
        <settings calloutType="simple">
          <text-style multilineHeight="1" fieldName="PL.PZGiK.201.32__OT_CIEK OT_Ciek_nazwa" fontCapitals="0" useSubstitutions="0" fontSize="500" textOrientation="horizontal" fontUnderline="0" fontWeight="50" fontKerning="1" textColor="17,150,206,255" blendMode="0" fontWordSpacing="0" namedStyle="Italic" fontFamily="Cambria" fontItalic="1" fontStrikeout="0" isExpression="0" fontSizeUnit="MapUnit" previewBkgrdColor="255,255,255,255" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0" textOpacity="1">
            <text-buffer bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferBlendMode="0" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferNoFill="1" bufferSize="0.7" bufferJoinStyle="128"/>
            <background shapeBlendMode="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeRadiiX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeRadiiUnit="MM" shapeDraw="0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSVGFile="" shapeRotation="0" shapeSizeType="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeType="0" shapeBorderWidthUnit="MM" shapeFillColor="255,255,255,255" shapeRadiiY="0"/>
            <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowRadiusUnit="MM" shadowOpacity="0.7" shadowDraw="0" shadowScale="100" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowBlendMode="6"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format useMaxLineLengthForAutoWrap="1" formatNumbers="0" decimals="3" placeDirectionSymbol="0" wrapChar="" multilineAlign="4294967295" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" autoWrapLength="0" addDirectionSymbol="0" reverseDirectionSymbol="0" plussign="0"/>
          <placement centroidInside="0" maxCurvedCharAngleIn="25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="UnknownGeometry" distUnits="MM" geometryGeneratorEnabled="0" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" yOffset="0" offsetUnits="MM" repeatDistance="0" repeatDistanceUnits="MM" placement="5" quadOffset="4" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" overrunDistance="0" xOffset="0" placementFlags="10" priority="5" centroidWhole="0" rotationAngle="0" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" distMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" offsetType="0"/>
          <rendering scaleMax="0" upsidedownLabels="0" drawLabels="1" fontMinPixelSize="3" obstacleFactor="1" fontLimitPixelSize="0" labelPerPart="0" obstacleType="0" mergeLines="0" zIndex="0" limitNumLabels="0" scaleVisibility="0" minFeatureSize="0" displayAll="0" maxNumLabels="2000" obstacle="1" scaleMin="0" fontMaxPixelSize="10000"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
              <Option name="drawToAllParts" type="bool" value="false"/>
              <Option name="enabled" type="QString" value="0"/>
              <Option name="lineSymbol" type="QString" value="&lt;symbol alpha=&quot;1&quot; name=&quot;symbol&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option name="minLength" type="double" value="0"/>
              <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="minLengthUnit" type="QString" value="MM"/>
              <Option name="offsetFromAnchor" type="double" value="0"/>
              <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
              <Option name="offsetFromLabel" type="double" value="0"/>
              <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule filter=" &quot;x_kodKarto250k&quot;  = '0250_602' and  &quot;PL.PZGiK.201.32__OT_ZBIORNIKWODNY OT_ZbiornikWodny_nazwa&quot;  = 'Morze Bałtyckie'" key="{2d9ca894-2c9a-49b4-aa79-03ada4867bb0}" description="Morze Bałtyckie">
        <settings calloutType="simple">
          <text-style multilineHeight="1" fieldName="PL.PZGiK.201.32__OT_ZBIORNIKWODNY OT_ZbiornikWodny_nazwa" fontCapitals="0" useSubstitutions="0" fontSize="1200" textOrientation="horizontal" fontUnderline="0" fontWeight="50" fontKerning="1" textColor="17,150,206,255" blendMode="0" fontWordSpacing="0" namedStyle="Italic" fontFamily="Cambria" fontItalic="1" fontStrikeout="0" isExpression="0" fontSizeUnit="MapUnit" previewBkgrdColor="255,255,255,255" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="3.15625" textOpacity="1">
            <text-buffer bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferBlendMode="0" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferNoFill="1" bufferSize="0.8" bufferJoinStyle="128"/>
            <background shapeBlendMode="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeRadiiX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeRadiiUnit="MM" shapeDraw="0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSVGFile="" shapeRotation="0" shapeSizeType="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeType="0" shapeBorderWidthUnit="MM" shapeFillColor="255,255,255,255" shapeRadiiY="0"/>
            <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowRadiusUnit="MM" shadowOpacity="0.7" shadowDraw="0" shadowScale="100" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowBlendMode="6"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format useMaxLineLengthForAutoWrap="1" formatNumbers="0" decimals="3" placeDirectionSymbol="0" wrapChar="" multilineAlign="4294967295" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" autoWrapLength="0" addDirectionSymbol="0" reverseDirectionSymbol="0" plussign="0"/>
          <placement centroidInside="0" maxCurvedCharAngleIn="25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="UnknownGeometry" distUnits="MM" geometryGeneratorEnabled="0" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" yOffset="0" offsetUnits="MM" repeatDistance="0" repeatDistanceUnits="MM" placement="4" quadOffset="4" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" overrunDistance="0" xOffset="0" placementFlags="10" priority="5" centroidWhole="0" rotationAngle="0" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" distMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" offsetType="0"/>
          <rendering scaleMax="0" upsidedownLabels="0" drawLabels="1" fontMinPixelSize="3" obstacleFactor="1" fontLimitPixelSize="0" labelPerPart="0" obstacleType="0" mergeLines="0" zIndex="0" limitNumLabels="0" scaleVisibility="0" minFeatureSize="0" displayAll="0" maxNumLabels="2000" obstacle="1" scaleMin="0" fontMaxPixelSize="10000"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
              <Option name="drawToAllParts" type="bool" value="false"/>
              <Option name="enabled" type="QString" value="0"/>
              <Option name="lineSymbol" type="QString" value="&lt;symbol alpha=&quot;1&quot; name=&quot;symbol&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option name="minLength" type="double" value="0"/>
              <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="minLengthUnit" type="QString" value="MM"/>
              <Option name="offsetFromAnchor" type="double" value="0"/>
              <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
              <Option name="offsetFromLabel" type="double" value="0"/>
              <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule filter=" &quot;x_kodKarto250k&quot;  = '0250_603'  AND  $area &lt;= 55000000" key="{27f69ea9-0772-432d-9e9b-06b463cb6b19}" description="Jezioro lub staw &lt; 55mln m2">
        <settings calloutType="simple">
          <text-style multilineHeight="1" fieldName="PL.PZGiK.201.32__OT_ZBIORNIKWODNY OT_ZbiornikWodny_nazwa" fontCapitals="0" useSubstitutions="0" fontSize="500" textOrientation="horizontal" fontUnderline="0" fontWeight="50" fontKerning="1" textColor="17,150,206,255" blendMode="0" fontWordSpacing="0" namedStyle="Italic" fontFamily="Cambria" fontItalic="1" fontStrikeout="0" isExpression="0" fontSizeUnit="MapUnit" previewBkgrdColor="255,255,255,255" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontLetterSpacing="0.1875" textOpacity="1">
            <text-buffer bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferBlendMode="0" bufferOpacity="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferNoFill="1" bufferSize="0.7" bufferJoinStyle="128"/>
            <background shapeBlendMode="0" shapeOffsetUnit="MM" shapeRotationType="0" shapeRadiiX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeRadiiUnit="MM" shapeDraw="0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSVGFile="" shapeRotation="0" shapeSizeType="0" shapeBorderWidth="0" shapeJoinStyle="64" shapeSizeY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBorderColor="128,128,128,255" shapeType="0" shapeBorderWidthUnit="MM" shapeFillColor="255,255,255,255" shapeRadiiY="0"/>
            <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetAngle="135" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowColor="0,0,0,255" shadowRadiusUnit="MM" shadowOpacity="0.7" shadowDraw="0" shadowScale="100" shadowOffsetDist="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowBlendMode="6"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format useMaxLineLengthForAutoWrap="1" formatNumbers="0" decimals="3" placeDirectionSymbol="0" wrapChar="" multilineAlign="4294967295" leftDirectionSymbol="&lt;" rightDirectionSymbol=">" autoWrapLength="0" addDirectionSymbol="0" reverseDirectionSymbol="0" plussign="0"/>
          <placement centroidInside="0" maxCurvedCharAngleIn="25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="UnknownGeometry" distUnits="MM" geometryGeneratorEnabled="0" overrunDistanceUnit="MM" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" geometryGeneratorType="PointGeometry" yOffset="0" offsetUnits="MM" repeatDistance="0" repeatDistanceUnits="MM" placement="4" quadOffset="4" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" overrunDistance="0" xOffset="0" placementFlags="10" priority="4" centroidWhole="0" rotationAngle="0" maxCurvedCharAngleOut="-25" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" geometryGenerator="" distMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" offsetType="0"/>
          <rendering scaleMax="0" upsidedownLabels="0" drawLabels="1" fontMinPixelSize="3" obstacleFactor="1.02" fontLimitPixelSize="0" labelPerPart="0" obstacleType="1" mergeLines="0" zIndex="0" limitNumLabels="0" scaleVisibility="0" minFeatureSize="4" displayAll="0" maxNumLabels="2000" obstacle="0" scaleMin="0" fontMaxPixelSize="10000"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
              <Option name="drawToAllParts" type="bool" value="false"/>
              <Option name="enabled" type="QString" value="0"/>
              <Option name="lineSymbol" type="QString" value="&lt;symbol alpha=&quot;1&quot; name=&quot;symbol&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot;>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option name="minLength" type="double" value="0"/>
              <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="minLengthUnit" type="QString" value="MM"/>
              <Option name="offsetFromAnchor" type="double" value="0"/>
              <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
              <Option name="offsetFromLabel" type="double" value="0"/>
              <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
    </rules>
  </labeling>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory width="15" minScaleDenominator="0" lineSizeType="MM" opacity="1" barWidth="5" scaleBasedVisibility="0" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" sizeScale="3x:0,0,0,0,0,0" minimumSize="0" backgroundColor="#ffffff" sizeType="MM" enabled="0" height="15" rotationOffset="270" backgroundAlpha="255" penWidth="0" scaleDependency="Area" maxScaleDenominator="1e+08" penAlpha="255" penColor="#000000">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="18" obstacle="0" zIndex="0" placement="1" priority="0" showAll="1" dist="0">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option name="allowedGapsBuffer" type="double" value="0"/>
        <Option name="allowedGapsEnabled" type="bool" value="false"/>
        <Option name="allowedGapsLayer" type="QString" value=""/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <fieldConfiguration>
    <field name="gml_id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lokalnyId">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="przestrzenNazw">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="wersja">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="poczatekWersjiObiektu">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="oznaczenieZmiany">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="zrodloDanychGeometrycznych">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="kodKarto250k">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="rodzaj">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="identyfikatorMPHP">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="nazwa">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="identyfikatorPRNG">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ZbiornikWodny1_gmlid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ciek2_gmlid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="gml_id" name=""/>
    <alias index="1" field="lokalnyId" name=""/>
    <alias index="2" field="przestrzenNazw" name=""/>
    <alias index="3" field="wersja" name=""/>
    <alias index="4" field="poczatekWersjiObiektu" name=""/>
    <alias index="5" field="oznaczenieZmiany" name=""/>
    <alias index="6" field="zrodloDanychGeometrycznych" name=""/>
    <alias index="7" field="kodKarto250k" name=""/>
    <alias index="8" field="rodzaj" name=""/>
    <alias index="9" field="identyfikatorMPHP" name=""/>
    <alias index="10" field="nazwa" name=""/>
    <alias index="11" field="identyfikatorPRNG" name=""/>
    <alias index="12" field="ZbiornikWodny1_gmlid" name=""/>
    <alias index="13" field="ciek2_gmlid" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" field="gml_id" applyOnUpdate="0"/>
    <default expression="" field="lokalnyId" applyOnUpdate="0"/>
    <default expression="" field="przestrzenNazw" applyOnUpdate="0"/>
    <default expression="" field="wersja" applyOnUpdate="0"/>
    <default expression="" field="poczatekWersjiObiektu" applyOnUpdate="0"/>
    <default expression="" field="oznaczenieZmiany" applyOnUpdate="0"/>
    <default expression="" field="zrodloDanychGeometrycznych" applyOnUpdate="0"/>
    <default expression="" field="kodKarto250k" applyOnUpdate="0"/>
    <default expression="" field="rodzaj" applyOnUpdate="0"/>
    <default expression="" field="identyfikatorMPHP" applyOnUpdate="0"/>
    <default expression="" field="nazwa" applyOnUpdate="0"/>
    <default expression="" field="identyfikatorPRNG" applyOnUpdate="0"/>
    <default expression="" field="ZbiornikWodny1_gmlid" applyOnUpdate="0"/>
    <default expression="" field="ciek2_gmlid" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" exp_strength="0" constraints="1" field="gml_id" notnull_strength="1"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="lokalnyId" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="przestrzenNazw" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="wersja" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="poczatekWersjiObiektu" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="oznaczenieZmiany" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="zrodloDanychGeometrycznych" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="kodKarto250k" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="rodzaj" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="identyfikatorMPHP" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="nazwa" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="identyfikatorPRNG" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="ZbiornikWodny1_gmlid" notnull_strength="0"/>
    <constraint unique_strength="0" exp_strength="0" constraints="0" field="ciek2_gmlid" notnull_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="gml_id" exp=""/>
    <constraint desc="" field="lokalnyId" exp=""/>
    <constraint desc="" field="przestrzenNazw" exp=""/>
    <constraint desc="" field="wersja" exp=""/>
    <constraint desc="" field="poczatekWersjiObiektu" exp=""/>
    <constraint desc="" field="oznaczenieZmiany" exp=""/>
    <constraint desc="" field="zrodloDanychGeometrycznych" exp=""/>
    <constraint desc="" field="kodKarto250k" exp=""/>
    <constraint desc="" field="rodzaj" exp=""/>
    <constraint desc="" field="identyfikatorMPHP" exp=""/>
    <constraint desc="" field="nazwa" exp=""/>
    <constraint desc="" field="identyfikatorPRNG" exp=""/>
    <constraint desc="" field="ZbiornikWodny1_gmlid" exp=""/>
    <constraint desc="" field="ciek2_gmlid" exp=""/>
  </constraintExpressions>
  <expressionfields>
    <field expression="regexp_substr( ZbiornikWodny1,'#(.*)')" subType="0" precision="0" name="ZbiornikWodny1_gmlid" length="250" type="10" comment="" typeName="string"/>
    <field expression="regexp_substr( ciek2,'#(.*)')" subType="0" precision="0" name="ciek2_gmlid" length="250" type="10" comment="" typeName="string"/>
  </expressionfields>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="&quot;PL.PZGiK.201.32__OT_Ciek_nazwa&quot;" sortOrder="1" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" hidden="0" name="gml_id" type="field"/>
      <column width="-1" hidden="0" name="lokalnyId" type="field"/>
      <column width="-1" hidden="0" name="przestrzenNazw" type="field"/>
      <column width="-1" hidden="0" name="poczatekWersjiObiektu" type="field"/>
      <column width="-1" hidden="0" name="rodzaj" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
      <column width="-1" hidden="0" name="ZbiornikWodny1_gmlid" type="field"/>
      <column width="-1" hidden="0" name="wersja" type="field"/>
      <column width="-1" hidden="0" name="oznaczenieZmiany" type="field"/>
      <column width="-1" hidden="0" name="zrodloDanychGeometrycznych" type="field"/>
      <column width="-1" hidden="0" name="kodKarto250k" type="field"/>
      <column width="-1" hidden="0" name="identyfikatorMPHP" type="field"/>
      <column width="-1" hidden="0" name="identyfikatorPRNG" type="field"/>
      <column width="-1" hidden="0" name="ciek2_gmlid" type="field"/>
      <column width="-1" hidden="0" name="nazwa" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Formularze QGIS mogą zawierać funkcje Pythona, które będą wywołane przy otwieraniu
 formularza.

Można z nich skorzystać, aby rozbudować formularz.

Wpisz nazwę funkcji w polu
"Python Init function".
Przykład:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="PL.PZGiK.201.32__OT_CIEK OT_Ciek_nazwa" editable="0"/>
    <field name="PL.PZGiK.201.32__OT_Ciek_nazwa" editable="0"/>
    <field name="PL.PZGiK.201.32__OT_ZBIORNIKWODNY OT_ZbiornikWodny_nazwa" editable="0"/>
    <field name="PL.PZGiK.201.32__OT_ZbiornikWodny_nazwa" editable="0"/>
    <field name="ZbiornikWodny1_gmlid" editable="0"/>
    <field name="ciek2" editable="1"/>
    <field name="ciek2_gmlid" editable="0"/>
    <field name="czyObiektBDOO" editable="1"/>
    <field name="gml_id" editable="1"/>
    <field name="idMPHP" editable="1"/>
    <field name="identyfikatorMPHP" editable="1"/>
    <field name="identyfikatorPRNG" editable="1"/>
    <field name="katIstnienia" editable="1"/>
    <field name="kodKarto250k" editable="1"/>
    <field name="lokalnyId" editable="1"/>
    <field name="nazwa" editable="1"/>
    <field name="oznaczenieZmiany" editable="1"/>
    <field name="poczatekWersjiObiektu" editable="1"/>
    <field name="przestrzenNazw" editable="1"/>
    <field name="rodzaj" editable="1"/>
    <field name="wersja" editable="1"/>
    <field name="wersjaId" editable="1"/>
    <field name="x_aktualnoscA" editable="1"/>
    <field name="x_aktualnoscG" editable="1"/>
    <field name="x_dataUtworzenia" editable="1"/>
    <field name="x_informDodatkowa" editable="1"/>
    <field name="x_katDoklGeom" editable="1"/>
    <field name="x_katIstnienia" editable="1"/>
    <field name="x_kod" editable="1"/>
    <field name="x_kodKarto1000k" editable="1"/>
    <field name="x_kodKarto100k" editable="1"/>
    <field name="x_kodKarto10k" editable="1"/>
    <field name="x_kodKarto250k" editable="1"/>
    <field name="x_kodKarto25k" editable="1"/>
    <field name="x_kodKarto500k" editable="1"/>
    <field name="x_kodKarto50k" editable="1"/>
    <field name="x_rodzajReprGeom" editable="1"/>
    <field name="x_skrKarto" editable="1"/>
    <field name="x_zrodloDanychA" editable="1"/>
    <field name="x_zrodloDanychG" editable="1"/>
    <field name="zbiornikWodny1" editable="1"/>
    <field name="zrodloDanychGeometrycznych" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="PL.PZGiK.201.32__OT_CIEK OT_Ciek_nazwa" labelOnTop="0"/>
    <field name="PL.PZGiK.201.32__OT_Ciek_nazwa" labelOnTop="0"/>
    <field name="PL.PZGiK.201.32__OT_ZBIORNIKWODNY OT_ZbiornikWodny_nazwa" labelOnTop="0"/>
    <field name="PL.PZGiK.201.32__OT_ZbiornikWodny_nazwa" labelOnTop="0"/>
    <field name="ZbiornikWodny1_gmlid" labelOnTop="0"/>
    <field name="ciek2" labelOnTop="0"/>
    <field name="ciek2_gmlid" labelOnTop="0"/>
    <field name="czyObiektBDOO" labelOnTop="0"/>
    <field name="gml_id" labelOnTop="0"/>
    <field name="idMPHP" labelOnTop="0"/>
    <field name="identyfikatorMPHP" labelOnTop="0"/>
    <field name="identyfikatorPRNG" labelOnTop="0"/>
    <field name="katIstnienia" labelOnTop="0"/>
    <field name="kodKarto250k" labelOnTop="0"/>
    <field name="lokalnyId" labelOnTop="0"/>
    <field name="nazwa" labelOnTop="0"/>
    <field name="oznaczenieZmiany" labelOnTop="0"/>
    <field name="poczatekWersjiObiektu" labelOnTop="0"/>
    <field name="przestrzenNazw" labelOnTop="0"/>
    <field name="rodzaj" labelOnTop="0"/>
    <field name="wersja" labelOnTop="0"/>
    <field name="wersjaId" labelOnTop="0"/>
    <field name="x_aktualnoscA" labelOnTop="0"/>
    <field name="x_aktualnoscG" labelOnTop="0"/>
    <field name="x_dataUtworzenia" labelOnTop="0"/>
    <field name="x_informDodatkowa" labelOnTop="0"/>
    <field name="x_katDoklGeom" labelOnTop="0"/>
    <field name="x_katIstnienia" labelOnTop="0"/>
    <field name="x_kod" labelOnTop="0"/>
    <field name="x_kodKarto1000k" labelOnTop="0"/>
    <field name="x_kodKarto100k" labelOnTop="0"/>
    <field name="x_kodKarto10k" labelOnTop="0"/>
    <field name="x_kodKarto250k" labelOnTop="0"/>
    <field name="x_kodKarto25k" labelOnTop="0"/>
    <field name="x_kodKarto500k" labelOnTop="0"/>
    <field name="x_kodKarto50k" labelOnTop="0"/>
    <field name="x_rodzajReprGeom" labelOnTop="0"/>
    <field name="x_skrKarto" labelOnTop="0"/>
    <field name="x_zrodloDanychA" labelOnTop="0"/>
    <field name="x_zrodloDanychG" labelOnTop="0"/>
    <field name="zbiornikWodny1" labelOnTop="0"/>
    <field name="zrodloDanychGeometrycznych" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>"gml_id"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
